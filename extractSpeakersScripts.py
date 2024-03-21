def extract_speaker_scripts(input_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as file:
        lines = file.readlines()

    speaker_scripts = {}
    # current_speaker = None
    # script = []
    speakers = []

    for line in lines:
        if line.startswith("<v"): 
            speaker_name = line.split('<v ')[1].split('>')[0].strip()
            script = line.split('>')[1].split('</v')[0].strip()
            if speaker_name not in speakers:
                speaker_scripts[speaker_name] = [script]
                speakers.append(speaker_name)
            else:
                speaker_scripts[speaker_name].append(script)

        else:
            continue 
        # elif line.startswith('</v>'):
        #     continue
        # elif line.startswith('0'):
        #     continue

    # Save each speaker's script to separate text files
    for speaker, script_lines in speaker_scripts.items():
        with open(f"{speaker}.txt", 'w', encoding=encoding) as out_file:
            out_file.write('\n'.join(script_lines))

if __name__ == "__main__":
    extract_speaker_scripts("everything.vtt", encoding='utf-8')