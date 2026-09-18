from enum import StrEnum


class PostmortemDocumentsAttachPayloadV1DocumentProvider(StrEnum):
    CONFLUENCE = "confluence"
    COPY_PASTE_BASECAMP = "copy_paste_basecamp"
    COPY_PASTE_CONFLUENCE = "copy_paste_confluence"
    COPY_PASTE_GITHUB_WIKI = "copy_paste_github_wiki"
    COPY_PASTE_GOOGLE_DOCS = "copy_paste_google_docs"
    COPY_PASTE_NOTION = "copy_paste_notion"
    COPY_PASTE_QUIP = "copy_paste_quip"
    GOOGLE_DOCS = "google_docs"
    INCIDENT_IO = "incident_io"
    NOTION = "notion"
    SHAREPOINT = "sharepoint"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
