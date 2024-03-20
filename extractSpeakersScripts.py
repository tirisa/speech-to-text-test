def extract_speaker_scripts(input_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as file:
        lines = file.readlines()

    speaker_scripts = {}
    current_speaker = None
    script = []

    for line in lines:
        if line.startswith("<v"):
            if current_speaker:
                speaker_scripts[current_speaker] = script

            current_speaker = line.split('<v ')[1].split('>')[0].strip()
            script = []

        elif line.startswith('</v>'):
            continue

        else:
            script.append(line.strip())

    # Save each speaker's script to separate text files
    for speaker, script_lines in speaker_scripts.items():
        with open(f"{speaker}.txt", 'w', encoding=encoding) as out_file:
            out_file.write('\n'.join(script_lines))

if __name__ == "__main__":
    extract_speaker_scripts("everything.vtt", encoding='utf-8')