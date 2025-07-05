from .BaseController import BaseController
from .ProjectController import ProjectController
import os 
from langchain_community.document_loaders import TerxtLoader
from langchain_community.document_loaders import PyMuPDFLoader 
from models import ProcesssingEnum
from langchain.text_splitter import RecursicveTextSplitter


class ProcessController(BaseController):
    def __init__(self , project_id : str):
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=self.project_id)

    def get_file_extention(self , file_id : str):
        return os.path.splitext(file_id)[-1] # return the extention of file
    
    def get_file_loader(self, file_id: str) :
        """
        Get the appropriate file loader based on the file extension.
        """
        file_ext = self.get_file_extention(file_id=file_id)
        file_path = os.path.join(self.project_path, file_id)  # full path of file
        
        if file_ext == ProcesssingEnum.TXT.value:
            return TerxtLoader(file_path , encoding = 'utf-8')
        elif file_ext == ProcesssingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        else:
            return None 
        

    def get_file_content(self, file_id: str):
        """
        Get the content of the file using the appropriate loader.
        """
        loader = self.get_file_loader(file_id=file_id)
        if loader:
            return loader.load()
        
        
    def process_file_content(self, file_content : list, file_id: str, chunk_size: int = 100, overlap_size: int = 200):
        """
        Process the file content and return the text.
        """
        documents = self.get_file_content(file_id=file_id)
        if documents:
            text_splitter = RecursicveTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap_size, length_function=len)

            file_content_texts = [
                rec.page_content
                for rec in file_content
            ]

            file_content_metadata = [
                rec.metadata
                for rec in file_content
            ]


            chunks = text_splitter.create_documents(
                file_content_texts,
                metadatas=file_content_metadata # for each chunk 
                )
            
            return chunks
        return None
        
