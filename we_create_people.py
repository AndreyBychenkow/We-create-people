import os
import random

from faker import Faker

import file_operations

current_dir = os.path.dirname(os.path.abspath(__file__))

template_path = os.path.join(current_dir, "output", "svg", "charsheet.svg")

output_dir = os.path.join(current_dir, "character cards")

skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]

letters_mapping = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


def generate_runic_skills(skills, letters_mapping):
    runic_skills = []
    for skill in skills:
        runic_skill = ''.join(letters_mapping.get(letter, letter)
                              for letter in skill)
        runic_skills.append(runic_skill)
    return runic_skills


def generate_character_context(runic_skills, fake):
    first_name = fake.first_name()
    last_name = fake.last_name()
    town = fake.city()
    job = fake.job()
    strength = random.randint(3, 18)
    agility = random.randint(3, 18)
    endurance = random.randint(3, 18)
    intelligence = random.randint(3, 18)
    luck = random.randint(3, 18)
    unique_skills = random.sample(runic_skills, 3)
    skill_1, skill_2, skill_3 = unique_skills

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "town": town,
        "job": job,
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3,
    }
    return context


def main():
    fake = Faker("ru_RU")
    runic_skills = generate_runic_skills(skills, letters_mapping)

    for i in range(10):
        context = generate_character_context(runic_skills, fake)

        output_filename = f"filled_character_card_{i + 1}.svg"
        output_path = os.path.join(output_dir, output_filename)
        file_operations.render_template(template_path, output_path, context)


if __name__ == '__main__':
    main()
