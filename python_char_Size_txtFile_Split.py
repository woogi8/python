def split_and_save_by_char_count(input_filename, output_prefix, char_count=20000):
    try:
        with open(input_filename, 'r') as original_file:
            content = original_file.read()
            total_chars = len(content)
            num_files = (total_chars + char_count - 1) // char_count

            for i in range(num_files):
                start_idx = i * char_count
                end_idx = min((i + 1) * char_count, total_chars)
                output_filename = f"{output_prefix}{i + 1}.txt"

                with open(output_filename, 'w') as output_file:
                    output_file.write(content[start_idx:end_idx])

                print(f"Saved {end_idx - start_idx} characters to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# 사용 예시:
input_file = "sepr.pc"  # 원본 텍스트 파일 이름
output_prefix = "output_sepr_"  # 새로운 파일 이름에 붙일 접두사

split_and_save_by_char_count(input_file, output_prefix,19000)
