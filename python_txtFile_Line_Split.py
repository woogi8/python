def split_and_save(input_filename, output_prefix, lines_per_file=500):
    try:
        with open(input_filename, 'r') as original_file:
            lines = original_file.readlines()
            total_lines = len(lines)
            num_files = (total_lines + lines_per_file - 1) // lines_per_file

            for i in range(num_files):
                start_idx = i * lines_per_file
                end_idx = min((i + 1) * lines_per_file, total_lines)
                output_filename = f"{output_prefix}{i + 1}.txt"

                with open(output_filename, 'w') as output_file:
                    output_file.writelines(lines[start_idx:end_idx])

                print(f"Saved {end_idx - start_idx} lines to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# 사용 예시:
input_file = "your_large_text_file.txt"  # 원본 텍스트 파일 이름
output_prefix = "output_"  # 새로운 파일 이름에 붙일 접두사

# 파일 저장 함수 - 맨뒤에 라인을 넣으면 라인수 만큼 처리해줌
split_and_save(input_file, output_prefix)
