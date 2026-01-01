import os
import sys
import pdfkit
from pathlib import Path

def find_wkhtmltopdf():
    """Находит путь к wkhtmltopdf"""
    # Возможные пути установки
    possible_paths = [
        r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        'wkhtmltopdf.exe',  # Если добавлен в PATH
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Попробуем найти в PATH
    import shutil
    try:
        wkhtmltopdf_path = shutil.which('wkhtmltopdf')
        if wkhtmltopdf_path:
            return wkhtmltopdf_path
    except:
        pass
    
    return None

def convert_html_to_pdf(html_file, pdf_file, wkhtmltopdf_path):
    """Конвертирует HTML файл в PDF используя pdfkit"""
    try:
        print(f"Конвертируем: {html_file}")
        print(f"В: {pdf_file}")
        
        # Настройки для конвертации
        options = {
            'page-size': 'A4',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None,
            'quiet': ''  # Уменьшаем вывод в консоль
        }
        
        # Конфигурация с явным указанием пути
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        
        # Конвертируем
        pdfkit.from_file(html_file, pdf_file, options=options, configuration=config)
        print(f"✓ Успешно создан: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"✗ Ошибка при конвертации {html_file}: {str(e)}")
        return False

def find_and_convert_html_files(root_directory, wkhtmltopdf_path):
    """Находит все HTML/HTM файлы и конвертирует их в PDF"""
    html_extensions = ('.html', '.htm')
    converted_count = 0
    error_count = 0
    
    print(f"Поиск HTML файлов в: {root_directory}")
    print(f"Используем wkhtmltopdf: {wkhtmltopdf_path}")
    print("-" * 80)
    
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(html_extensions):
                html_path = os.path.join(root, file)
                
                # Создаем имя для PDF файла
                pdf_filename = os.path.splitext(file)[0] + '.pdf'
                pdf_path = os.path.join(root, pdf_filename)
                
                # Пропускаем если PDF уже существует
                if os.path.exists(pdf_path):
                    print(f"↷ Пропускаем (уже существует): {pdf_path}")
                    continue
                
                # Конвертируем
                if convert_html_to_pdf(html_path, pdf_path, wkhtmltopdf_path):
                    converted_count += 1
                else:
                    error_count += 1
                print()  # Пустая строка между файлами
    
    print("=" * 80)
    print(f"Конвертация завершена!")
    print(f"✓ Успешно: {converted_count}")
    print(f"✗ С ошибками: {error_count}")

def main():
    if len(sys.argv) != 2:
        print("Использование: python html_to_pdf_converter.py <папка>")
        print("Пример: python html_to_pdf_converter.py ./my_folder")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    
    if not os.path.exists(root_directory):
        print(f"Ошибка: Папка '{root_directory}' не существует!")
        sys.exit(1)
    
    if not os.path.isdir(root_directory):
        print(f"Ошибка: '{root_directory}' не является папкой!")
        sys.exit(1)
    
    # Находим wkhtmltopdf
    wkhtmltopdf_path = find_wkhtmltopdf()
    
    if not wkhtmltopdf_path:
        print("Ошибка: wkhtmltopdf не найден!")
        print("Пожалуйста, установите wkhtmltopdf:")
        print("1. Скачайте с: https://wkhtmltopdf.org/downloads.html")
        print("2. Установите в папку по умолчанию")
        print("3. Или укажите путь вручную в переменной wkhtmltopdf_path")
        sys.exit(1)
    
    print("HTML to PDF Converter (pdfkit + wkhtmltopdf)")
    print("=" * 80)
    find_and_convert_html_files(root_directory, wkhtmltopdf_path)

if __name__ == "__main__":
    main()