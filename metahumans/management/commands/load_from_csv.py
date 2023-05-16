#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv

from django.core.management.base import BaseCommand, CommandError

from metahumans.models import Identity, Team, Power, Metahuman


def name_to_foto_filename(name):
    trans = str.maketrans({
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ñ': 'n',
        ' ': '_',
        'Á': 'a',
        'É': 'e',
        'Í': 'i',
        'Ó': 'o',
        'Ú': 'u',
        'Ñ': 'n',
        })
    name = name.lower().translate(trans)
    return f'metahumans/{name}.png'


class Command(BaseCommand):
    help = 'Rellena la base de datos a partir de un fichero CSV'

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def error_file_not_exists(self, filename):
        raise CommandError(f"No existe el fichero f{filename}")

    def handle(self, *args, **options):
        filename = options.get('filename')
        if not os.path.exists(filename):
            self.error_file_not_exists(filename)
        print(f"Importando metahumanos desde {filename}")
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            counter = 0
            for row in reader:
                name = row['name']
                print(f" - Creando metahumano {name}", end=' ', flush=True)
                if Metahuman.objects.filter(name=name).exists():
                    print("[skipped]")
                    continue
                first_name = row['first_name']
                last_name = row['last_name']
                identity, _ = Identity.objects.get_or_create(
                    first_name=first_name,
                    last_name=last_name,
                    )
                photo = name_to_foto_filename(name)
                level = int(row['level'])
                metahuman = Metahuman(
                    name=name,
                    identity=identity,
                    level=level,
                    photo=photo,
                    )
                team_name = row['team'].title().strip()
                if team_name:
                    headquarter = row['headquarter']
                    team, _ = Team.objects.get_or_create(
                        name=team_name,
                        headquarter=headquarter,
                        )
                    metahuman.team = team
                powers_set = set([])
                for power_name in row['powers'].split(","):
                    power_name = power_name.strip().lower()
                    power, _ = Power.objects.get_or_create(
                        name=power_name,
                        )
                    powers_set.add(power)
                    print(".", end="", flush=True)
                metahuman.save()
                metahuman.powers.set(powers_set)
                metahuman.save()
                counter += 1
                print("[ok]")
        print(f"Importados {counter} metahumanos a la base de datos")
