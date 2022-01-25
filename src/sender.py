import telebot
from datetime import datetime as date
from PIL import Image

# Paths and message for sender to use
info_path = 'src/info.txt'
path = 'data/covid_cases_graph.png'
save_path = 'data/covid_cases_graph_telegram.png'
message = 'RIT COVID-19 Positive Cases:  ' + str(date.today().strftime("%B %d, %Y")) + '\n-Max'


# Main script that reads info files for information and
# uses it to send the image and message to the selected
# user.
def main() -> None:
    with open(info_path) as f:
        lines = f.readlines()

    stripped_lines = []
    for line in lines:
        stripped_lines.append((line.strip()))

    token = str(stripped_lines[0])

    control = int(stripped_lines[1])
    send = int(stripped_lines[2])
    send_group = int(stripped_lines[3])

    bot = telebot.TeleBot(token, parse_mode=None)

    photo = Image.open(path)
    new_photo = photo.resize((1280, 960))
    new_photo.save(save_path)

    send_photo = open(save_path, 'rb')
    bot.send_photo(control, send_photo)

    bot.send_message(control, message)


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
