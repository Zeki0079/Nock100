import re
import p20

# カテゴリ名を宣言している行を抽出;長くなるから国名指定する


def extract_category_sentence(title_str):
    # 問題20の関数を使用して記事を取得
    text_contents = p20.get_text_from_json(title_str)
    text_sentences = text_contents.split('\n')

    for line in text_sentences:
        pattern_media_file = re.search(r'.+ファイル.+', line)
        if pattern_media_file != None:
            # [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]　の形式にどれもなっている
            # ファイル: 〜 |の間を取り除けばいいことがわかる、前半部分を:だけにすると変なurlも含まれた
            media_file = re.sub(r'.+ファイル:|\|.+', '', pattern_media_file.group())
            print(media_file)
    return


extract_category_sentence("イギリス")


'''
21 p.63 質問されそうなことを想像する

実行結果
Royal Coat of Arms of the United Kingdom.svg
United States Navy Band - God Save the Queen.ogg]]}}
Descriptio Prime Tabulae Europae.jpg
Lenepveu, Jeanne d'Arc au siège d'Orléans.jpg
London.bankofengland.arp.jpg
Battle of Waterloo 1815.PNG
Uk topo en.jpg
BenNevis2005.jpg
Population density UK 2011 census.png
Birmingham Skyline from Edgbaston Cricket Ground crop.jpg
Glasgow and the Clyde from the air (geograph 4665720).jpg
Palace of Westminster, London - Feb 2007.jpg
Scotland Parliament Holyrood.jpg
Donald Trump and Theresa May (33998675310) (cropped).jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Airbus A380-841 G-XLEB British Airways (10424102995).jpg
UKpop.svg
Anglospeak.svg
Royal Aberdeen Children's Hospital.jpg
CHANDOS3.jpg
The Fabs.JPG
Wembley Stadium, illuminated.jpg
'''