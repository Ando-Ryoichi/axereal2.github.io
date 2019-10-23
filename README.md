# axereal2.github.io

[https://axereal.net](https://axereal.net)

## リポジトリ構成

| path | 説明|
|:-:|:-:|
| [_includes/about.html](/_includes/about.html) | Aboutの部分のHTML |
| [_includes/company.html](/_includes/company.html) | 会社概要の部分のHTML |
| [_includes/contact.html](/_includes/contact.html) | お問い合わせの部分のHTML |
| [_includes/footer.html](/_includes/footer.html) | フッター部分のHTML |
| [_includes/head.html](/_includes/head.html) | CSSの読み込みなど |
| [_includes/header.html](/_includes/header.html) | ヘッダー部分のHTML |
| [_includes/navbar.html](/_includes/navbar.html) | ナビゲーションバー部分のHTML |
| [_includes/news.html](/_includes/news.html) | ニュース部分のHTML |
| [_includes/portfolio.html](/_includes/portfolio.html) | スポーツの部分のHTML |
| [_includes/scripts.html](/_includes/scripts.html) | JSの読み込みなど |
| [_includes/services.html](/_includes/services.html) | 事業内容の部分のHTML |
| [_includes/sponsor.html](/_includes/sponsor.html) | 協力団体の部分のHTML |
| [_layouts/home.html](/_layouts/home.html) | 大枠。 [_includes/](/_includes/)の中のHTMLを組み合わせて全体を構成する。 |
| [_posts/](/_posts/) | ニュース記事のmarkdownファイルを追加する場所。 |
| [img/posts/](/img/posts/) | ニュース記事に使う画像ファイルを追加する場所。 |

## Webサイトへのニュースの追加方法

### 1. markdownファイルの作成
まずmarkdownで記事を作成します。例えば次のような記事を書いたとします。

```markdown
---
layout: post
title: "○○展への出展のお知らせ"
subtitle: ""
author: kanta mori
date:   2019-10-23 16:30:13 +0900
background: '/img/posts/default.jpg'
---

この度、弊社が開発、普及を進めているスポーツ、ゴーンボールが○○展へ出展されることになりました。ふるってご参加ください。

## 開催概要
「○○展」

## 内容
~~~

## 日時
2017年7月15日(土)
10：00開場　10：30－19：00頃

2017年7月16日(日)
10：00開場　10：00－19：00頃

## 会場
幕張メッセ

## 参加費
無料（どなたでも参加いただけますが、事前申込が必要です。）

## 参加申込方法
7月13日（木）までに、次のE-Mailアドレスあて所要事項を記入のうえ送信願います。
E-Mailアドレス：contact@example.com
所要事項：（1）氏名、（2）職業・勤務先（学生の場合は学校・学科・学年）、（3）電話番号

## 主催・協力
超人スポーツ協会
```

ここで、ファイル先頭にある`---`(ハイフン3つ)で囲まれている部分は記事のメタデータです。subtitleとauthor以外は必須項目なので書き忘れないようにしてください(忘れるとサーバー側でエラーが発生する可能性があります)。layoutはpostのままでいじらず、titleとdate, backgroundを記事に合わせて書き換えてください。

backgroundは、ニュース記事のサムネイルに使う画像ファイルを指定するものです。使いたい画像を[/img/posts](/img/posts)にアップロードした上で上のように指定します。特に指定がない場合でも、[/img/posts/default.jpg](/img/posts/default.jpg)などを使うなどしてください。

ファイルを作成し終わったら、ファイル名を以下のようなフォーマットにして保存します。

```
YEAR-MONTH-DAY-title.md
```

titleの部分には記事のタイトルを指定することができますが、既にmarkdownファイル中にメタデータで指定しているので適当な文字で大丈夫です(逆に、ここに日本語でタイトルを入れてしまうとサーバー側で全角文字を処理する際にエラーが起きる可能性があるので、titleのままの方が良いと思います)。

今回の例では次のようなファイル名にしておきます。

```
2019-10-23-title.md
```

### 2. GitHubへの記事のアップロード
記事のmarkdownファイルが作成できたら、それをGitHubにアップロードします。方法としては、

1. ブラウザからアップロードする方法
2. GitHub Desktopからアップロードする方法
3. コマンドラインからアップロードする方法

などがありますが、ここではブラウザからアップロードする方法を取り上げます。まずブラウザで[https://github.com/tuz358/axereal2.github.io](https://github.com/tuz358/axereal2.github.io)を開きます。

![/img/sshot1.png](/img/sshot1.png)

開いたら、上のように`_posts`ディレクトリをクリックします。

![`_posts`をクリックした所](/img/sshot2.png)

すると上のような画面になるので、`Upload files`ボタンをクリックします。

![`Upload files`をクリックした所](/img/sshot3.png)

後は画面の指示に従ってファイルを選択してコミットメッセージを入力し、最後に下の`Commit changes`ボタンを押せば完了です。

## markdownの文法

### テキスト

#### markdown

```markdown
普通の文章。
```

#### 出力結果

普通の文章。

### 改行

改行したい行の間に空行を入れる。

#### markdown

```markdown
文章1。
(空行)
文章2。
```

#### 出力結果

文章1。

文章2。

### 見出し

#### markdown

```markdown
# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
```

#### 出力結果

# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6

### リスト

#### markdown

```markdown
- item1
- item2
- item3

* item1
* item2
* item3

1. item1
2. item2
3. item3

- item1
    - item1-1
    - item1-2
- item2
    - item2-1
    - item2-2
```

#### 出力結果

- item1
- item2
- item3

* item1
* item2
* item3

1. item1
2. item2
3. item3

- item1
    - item1-1
    - item1-2
- item2
    - item2-1
    - item2-2

### リンク

#### markdown

```markdown
[リンク](http://example.com)
```

#### 出力結果

[リンク](http://example.com)

### テーブル

#### markdown
```markdown
| 左寄せ | 中央 | 右寄せ |
|:-----|:----:|---:|
| テキスト | *テキスト* | **テキスト** |
| テキスト | `テキスト` | テキスト |
```

#### 出力結果

| 左寄せ | 中央 | 右寄せ |
|:-----|:----:|---:|
| テキスト | *テキスト* | **テキスト** |
| テキスト | `テキスト` | テキスト |

### 画像

#### markdown

```markdown
![代替テキスト](https://github.com/favicon.ico "キャプション")
```

#### 出力結果

![代替テキスト](https://github.com/favicon.ico "キャプション")

### 強調

`*`が1つでイタリック、2つで太字、3つでイタリック+太字。

#### markdown

```markdown
*強調したい箇所*

**強調したい箇所**

***強調したい箇所***
```

#### 出力結果

*強調したい箇所*

**強調したい箇所**

***強調したい箇所***

### 打ち消し

#### markdown

```markdown
~~打ち消したい箇所~~
```

#### 出力結果

~~打ち消したい箇所~~

### 注釈

#### markdown

```markdown
説明[^1]

[^1] : 補足
```

#### 出力結果

説明[^1]

[^1] : 補足

### 引用

#### markdown

```markdown
> 引用する文章
> 引用する文章
>
> 引用する文章

> 引用する文章
>> 引用する文章(入れ子)
```

#### 出力結果

> 引用する文章
> 引用する文章
>
> 引用する文章

> 引用する文章
>> 引用する文章(入れ子)

### チェックボックス

#### markdown

```markdown
- [ ] チェックボックス1
- [x] チェックボックス2
```

#### 出力結果

- [ ] チェックボックス1
- [x] チェックボックス2

### 水平線
`*`、`-`、`_`のどれかを3つ以上並べればOK。

#### markdown

```markdown
---
***
___
* * *
```

#### 出力結果

---
***
___

* * *
