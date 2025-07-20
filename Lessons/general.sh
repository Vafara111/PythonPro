##!1/bin/bash
#
#echo "введіть своє ім'я"
#read username
#echo "привіт $username"
#
#echo "введіть ім'я файлу"
#read filename
#if [-f "$filename"]; then
#  echo "Файл вже існує"
#else
#  echo "Файлу не існує"
#  echo "Створюємо файл '$filename'..."
#  touch $filename
#fi
#
#echo "Цикл"
#
#for i in {1..6}
#do
#  echo "Число: $i"
#done
#
#echo "Вкажіть назву файлу для бекапу!"
#read filename
#
#backup_file="$filename-$(date +Ymd).backup"
#if [ -f filename ]; then
#  cp "$filename" "$backup_file"
#  echo "Створємо резервну копію $backup_file"
#else
#  echo "Помилка: файл $backup_file не знайдено"
#fi
#
echo "Files count"
current_dir=$(pwd)
file_count=$(ls -l | grep ^- | wc -l)
echo "Dir $current_dir contains a $file_count files"

echo "Enter env name"
read python_env

if [ -f "requirements.txt" ]; then
  echo "Installing requirements processing..."
  python3 -m venv $python_env
  $python_env/Scripts/activate
  pip install -r requirements.txt
  deactivate
  echo "All packages installed into venv $python_env"
else
  echo "requirements.txt not found"
fi