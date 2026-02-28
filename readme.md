# 小説コーパスAPI
[株式会社グロービスによる青空文庫のテキストコーパス](https://huggingface.co/datasets/globis-university/aozorabunko-clean)から取得した夏目漱石の作品から作成した単語のテキストデータからja_ginzaを用いて形態素解析・係り受け解析を実施し、そのデータをもとにした単語の共起データを返すAPIです。
今後は、他の著者の作品にも拡大する予定です。

## こちらを利用したウェブサイト
(日本語小説共起語データべースのリポジトリ)[https://github.com/Kodai1000/japanese_novel_corpus_word_profile]

## API
1. /co_occurrence/夏目漱石/all/<word>/<minimum_count>
    単語<word>と共起する語で、設定された最小共起回数<minimm_count>以上のものを返す。
    ※allの部分には、今後係り受けの関係を入力できるようにする予定です。
2. /get_relative_words/夏目漱石/<keyword>
    データベースに登録されている単語のうち、文字列<keyword>と一部一致する単語を返す。