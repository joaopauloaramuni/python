import shutil
from pathlib import Path
from engine.service.organizer_service import OrganizerService

def test_organization():
    test_dir = Path("test_organizer")
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    # Create dummy files
    (test_dir / "file1.pdf").write_text("dummy")
    (test_dir / "file2.jpg").write_text("dummy")
    (test_dir / "file3.mp4").write_text("dummy")
    (test_dir / "file4.zip").write_text("dummy")
    (test_dir / "file5.unknown").write_text("dummy")
    (test_dir / "duplicate.pdf").write_text("original")
    
    # Create another folder to test duplicate names
    pdf_dir = test_dir / "PDFs"
    pdf_dir.mkdir()
    (pdf_dir / "duplicate.pdf").write_text("already here")

    print(f"Arquivos criados em {test_dir.absolute()}")

    service = OrganizerService()
    
    def log_callback(progress, msg):
        print(f"[{progress:.1f}%] {msg}")

    print("\nIniciando organização...")
    service.organize_directory(str(test_dir), progress_callback=log_callback)

    # Verification
    print("\nVerificando resultados:")
    expected_folders = ["PDFs", "Imagens", "Vídeos", "Compactados", "Outros"]
    all_ok = True
    
    for folder in expected_folders:
        folder_path = test_dir / folder
        if folder_path.exists() and folder_path.is_dir():
            print(f"[OK] Pasta '{folder}' criada.")
        else:
            print(f"[FAIL] Pasta '{folder}' NÃO encontrada.")
            all_ok = False

    # Check for renamed file
    renamed_file = test_dir / "PDFs" / "duplicate (1).pdf"
    if renamed_file.exists():
        print("[OK] Arquivo duplicado renomeado corretamente.")
    else:
        print("[FAIL] Arquivo duplicado NÃO renomeado.")
        all_ok = False

    if all_ok:
        print("\nTESTE CONCLUÍDO COM SUCESSO!")
    else:
        print("\nTESTE FALHOU!")

    # Cleanup
    # shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_organization()
