     f.write(content)
                        msg = f"✅ Đã sửa file: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                    else:
                        msg = f"⚠️ Không tìm thấy chuỗi trong: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                except Exception as e:
                    msg = f"❌ Lỗi với file {full_path}: {e}"
                    print(msg)
                    log_entries.append(msg)
