import re
import argparse
import pandas as pd
from datetime import date

def generate_lectures(sched, link):
    lecture_dates = [s['date'] for _, s in sched.iterrows() if s['lecture']]
    lecture_topics = [s['topic'].strip() for _, s in sched.iterrows() if s['lecture']]

    for i, (date, topic) in enumerate(zip(lecture_dates, lecture_topics), start=1):
        text = f"---\npublished: true\nnumber: {i}\ndate: {date}\ntime: 9:00\ntitle: \"{topic}\"\nurl: {link}\n---"
        with open(f'_lectures/{i:02d}.md', '+w') as f:
            f.write(text)

def generate_modules(sched):
    weeks = {index: group for index, group in sched.groupby('week_index')}

    for week in weeks:
        module = weeks[week]
        content = f"---\ntitle: Week {week}\n---\n"
        for _, day in module.iterrows():
            content += f"\n{pd.to_datetime(day['date']).strftime('%b %-d')}\n"
            if day['lecture']:
                content += f": {{% lec {day['lecture']} %}}\n"
            notes = day['notes'].lower().split(',')
            for note in notes:
                if note == '':
                    continue
                if 'lab' not in note:
                    content += f': **{note.strip()}**{{: .label .label-break }}\n'
                    continue

                lab = re.search(r'lab (\d+)', note)[0]
                lab_key = lab.replace(' ', '')
                text = note.replace(lab, '').strip() if 'checkpoint' in note else note.strip()
                if 'due' in note:
                    content += f': **{text}**{{: .label .label-{lab_key} }}\n'
                if 'released' in note:
                    content += f': {{% {lab} %}}\n'

        with open(f'_modules/week-{week:02d}.md', '+w') as f:
            f.write(content)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', type=str, default='schedule.csv')
    parser.add_argument('--github_link', '-l', type=str, default='https://github.com/ucb-datalab/course_materials_sp2026/tree/main/lectures')
    
    args = parser.parse_args()
    year = current_year = date.today().year
    sched = pd.read_csv(args.filename, header=None, names=['lecture', 'date', 'topic', 'notes'], keep_default_na=False)
    sched['date'] = [f'{year}-'+s['date'].replace('/', '-').replace(" ", '') for _, s in sched.iterrows()]
    sched['week_index'] = pd.to_datetime(sched['date']).dt.isocalendar().week
    sched['week_index'] -= sched['week_index'].min()

    generate_lectures(sched, args.github_link)
    generate_modules(sched)