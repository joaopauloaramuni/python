import logging
import shutil
from pathlib import Path
from typing import Callable, Optional
from engine.config.settings import FILE_CATEGORIES, DEFAULT_OTHER_FOLDER
from engine.utils.file_utils import get_unique_path, categorize_file

class OrganizerService:
    def __init__(self):
        self.categories = FILE_CATEGORIES
        self.default_folder = DEFAULT_OTHER_FOLDER

    def organize_directory(
        self, 
        directory_path: str, 
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> bool:
        """
        Organizes files in the given directory into categorized subfolders.
        """
        base_path = Path(directory_path)
        
        if not base_path.exists() or not base_path.is_dir():
            if progress_callback:
                progress_callback(0, f"Erro: Caminho inválido {directory_path}")
            return False

        # Get all files (excluding directories)
        files = [f for f in base_path.iterdir() if f.is_file()]
        total_files = len(files)
        
        if total_files == 0:
            if progress_callback:
                progress_callback(100, "Nenhum arquivo encontrado para organizar.")
            return True

        processed_count = 0
        
        for file_path in files:
            try:
                # Determine destination folder
                category = categorize_file(file_path.suffix, self.categories, self.default_folder)
                destination_dir = base_path / category
                
                # Create destination folder if it doesn't exist
                destination_dir.mkdir(exist_ok=True)
                
                # Determine destination file path (handling name collisions)
                destination_path = destination_dir / file_path.name
                final_path = get_unique_path(destination_path)
                
                # Move the file
                shutil.move(str(file_path), str(final_path))
                
                processed_count += 1
                if progress_callback:
                    percentage = (processed_count / total_files) * 100
                    msg = f"Movido: {file_path.name} -> {category}/"
                    logging.info(f"Movido: {file_path.name} -> {category}/")
                    if final_path.name != file_path.name:
                        msg += f" (renomeado para {final_path.name})"
                    progress_callback(percentage, msg)
                    
            except Exception as e:
                if progress_callback:
                    progress_callback((processed_count / total_files) * 100, f"Erro ao mover {file_path.name}: {str(e)}")

        if progress_callback:
            progress_callback(100, f"Sucesso! {processed_count} arquivos organizados.")
            
        return True
