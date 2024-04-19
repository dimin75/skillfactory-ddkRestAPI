import yaml

def yaml_to_markdown(yaml_str):
    data = yaml.safe_load(yaml_str)
    markdown = f"# {data['info']['title']}\n\n"
    markdown += f"## {data['info']['description']}\n\n"
    markdown += f"* Версия: {data['info']['version']}\n"
    # markdown += f"* Условия использования: [{data['info']['termsOfService']}]({data['info']['termsOfService']})\n"
    markdown += f"* Контакт: {data['info']['contact']['email']}\n"
    markdown += f"* Лицензия: {data['info']['license']['name']}\n\n"
    markdown += "### Базовая информация\n\n"
    markdown += f"* Хост: {data['host']}\n"
    markdown += f"* Протоколы: {', '.join(data['schemes'])}\n"
    markdown += f"* Базовый путь: {data['basePath']}\n\n"
    markdown += "### Форматы данных\n\n"
    markdown += f"* Входные данные: {', '.join(data['consumes'])}\n"
    markdown += f"* Выходные данные: {', '.join(data['produces'])}\n\n"
    markdown += "### Безопасность\n\n"
    markdown += f"* Описание: {', '.join(data['securityDefinitions'])}\n\n"
    markdown += "## Маршруты\n\n"
    for path, path_data in data['paths'].items():
        markdown += f"### {path}\n\n"
        for method, method_data in path_data.items():
            markdown += f"#### {method.upper()} {path}\n\n"
            if isinstance(method_data, list):
                continue  # Пропускаем список, так как не можем получить описание
            markdown += f"* Описание: {method_data.get('description', '')}\n"
            if 'parameters' in method_data:
                markdown += "* Параметры:\n"
                for param in method_data['parameters']:
                    markdown += f"  - {param['name']}: {'обязательный' if param.get('required', False) else 'необязательный'}, {param['type']}, в {param['in']}\n"
            if 'responses' in method_data:
                markdown += "* Ответ:\n"
                for resp_code, resp_data in method_data['responses'].items():
                    markdown += f"  - {resp_code}: {resp_data['description']}\n"
            markdown += "\n"
    return markdown

# Пример использования:
with open("docdownloaded.yaml", "r", encoding="utf-8") as f:
    yaml_str = f.read()

markdown_output = yaml_to_markdown(yaml_str)

# Запись результата в файл
with open("README.md", "w") as f:
    f.write(markdown_output)
