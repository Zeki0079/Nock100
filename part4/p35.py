import p30

# 単語の出現頻度を高い順に並べたリストを返す

def return_sort_word_frequency_list(file_input_name):
    word_dict = {}
    word_list = []
    sentence_mecab_list = p30.convert_mecab_to_list(file_input_name)

    # 単語の基本形の出現回数を辞書を用いてカウント
    for list in sentence_mecab_list:
        for dict in list:
            base_str = dict.get("base")
            if base_str in word_dict.keys():
                word_dict[base_str] += 1
            else:
                word_dict[base_str] = 1

    # 辞書の値で降順にソートし、キーを新たなリストに格納して返す
    freq_base_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    #for list in freq_base_list:
        #word_list.append(list[0])
    return freq_base_list

'''
print(return_sort_word_frequency_list("neko.txt.mecab"))
'''

'''
p.21 値の属性を追加する

実行結果　５０個
['の', 'だ', '。', 'て', '、', 'は', 'と', 'を', 'に', 'が', 'た', 'する', 'も', '「', '」', 'ない', 'で', 'ある', 'から', 'か', 'いる', 'ぬ',
'云う', '事', 'です', 'ます', 'なる', 'もの', 'へ', '君', '主人', 'ん', '何', '御', '見る', 'よう', 'ね', '—', 'この', 'その', 'それ', 'ば', 
'そう', '思う', 'よ', '人', '吾輩', '一', 'これ', '来る']

[('の', 9547), ('だ', 8273), ('。', 7486), ('て', 7384), ('、', 6773), ('は', 6500), ('と', 6155), ('を', 6119), ('に', 5695), ('が', 5396),
('た', 4276), ('する', 3866), ('も', 3253), ('「', 3238), ('」', 3238), ('ない', 3083), ('で', 2530), ('ある', 2304), ('から', 2212), ('か', 2043),
('いる', 1672), ('ぬ', 1586), ('云う', 1397), ('事', 1212), ('です', 1166), ('ます', 1156), ('なる', 1071), ('もの', 1004), ('へ', 995), ('君', 971), 
('主人', 934), ('ん', 729), ('何', 715), ('御', 706), ('見る', 688), ('よう', 683), ('ね', 669), ('—', 666), ('この', 657), ('その', 620), ('それ', 612), 
('ば', 600), ('そう', 570), ('思う', 511), ('よ', 497), ('人', 485), ('吾輩', 481), ('一', 478), ('これ', 471), ('来る', 470)]

'''