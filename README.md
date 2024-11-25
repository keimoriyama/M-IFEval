# IFEval: Instruction Following Eval

This is not an officially supported Google product.

This repository contains source code and data for
[Instruction Following Evaluation for Large Language Models](arxiv.org/abs/2311.07911)

## Dependencies

Please make sure that all required python packages are installed via:

```
pip3 install -r requirements.txt
```

## How to run

You need to create a jsonl file with two entries: prompt and response.
Then, call `evaluation_main` from the parent folder of
instruction_following_eval. For example:

```bash
# Content of `--input_response_data` should be like:
# {"prompt": "Write a 300+ word summary ...", "response": "PUT YOUR MODEL RESPONSE HERE"}
# {"prompt": "I am planning a trip to ...", "response": "PUT YOUR MODEL RESPONSE HERE"}
# ...
python3 -m evaluation_main \
  --input_data=./data/input_data.jsonl \
  --input_response_data=./data/input_response_data_gpt4_20231107_145030.jsonl \
  --output_dir=./evaluation/
```

## Reference

If you use our work, please consider citing our preprint:

```
@article{zhou2023instruction,
  title={Instruction-Following Evaluation for Large Language Models},
  author={Zhou, Jeffrey and Lu, Tianjian and Mishra, Swaroop and Brahma, Siddhartha and Basu, Sujoy and Luan, Yi and Zhou, Denny and Hou, Le},
  journal={arXiv preprint arXiv:2311.07911},
  year={2023}
}
```

## 日本語データセットについて

日本語特有のinstructionsは次の通りです。
| Instruction Group | Instruction | Description|
| --- | --- | --- |
| Length Constraints | Number Letters | {N}文字以上 / 未満で答えてください。 |
| Punctuation | No Periods | 応答全体で句点を使用しないでください。 |
| Letters | Furigana | 全ての漢字にふりがなをつけてください。ふりがなは全角の括弧（）の中に書いてください。 |
| Letters | Kanji | {N}文字以上 / 未満漢字を用いて答えてください。 |
| Letters | No Hiragana | ひらがなを一文字も使わないで答えてください。 |
| Letters | Hiragana Only | ひらがなだけを用いて答えてください。 |
| Letters | No Katakana | カタカナを一文字も使わないで答えてください。 |
| Letters | Katakana Only | カタカナだけを用いて答えてください。 |
| Letters | Unified Sentence Endings | 応答において、全ての文末が「{ending}」で統一された自然な文章にしてください。 |
| Letters | Kansuuji | 数字を全て漢数字で表記してください。 |
| Detectable Format | Nominal Endings | 応答の中で体言止めを{N}回は使用してください。 |
| Detectable Format | Numbered Lists | 応答はちょうど {N} 個の番号付きリストで構成してください。以下のような番号付きリストの形を参考にしてください: 1. 一つめの内容 ... |

日本語のプロンプトは3つのステップで作成されました。
まず、Few-shotプロンプティングを用いて、この課題に適切なプロンプトを書くように教育しました。
次に、なるべくランダムなテーマとプロンプトに組み込みたい条件文を指定することで、条件に合ったプロンプトを10個書かせました。
最後に、それらから適切なプロンプトを手動で書き換えることで、プロンプト文をコードに書き加えました。

## French Dataset

The French-specific instructions are as follows:

| Instruction Group | Instruction | Description| Translation |
| --- | --- | --- | --- |
| Special Character | Forbidden Character (Ethel or Cedilla) | N'incluez pas le caractère {forbidden_char} dans votre réponse. | Do not include the character {forbidden_char} in your answer.
| Special Character | No Accents | Ne faites pas usage d'accents dans votre réponse. | Do not use accents in your answer. |
| Special Character | Add Accents | Réécris ce texte en ajoutant les accents. | Rewrite this text by adding the accents. | 
| Detectable Content | Informal Address | Parlez directement à votre interlocuteur dans votre réponse et utilisez le tutoiement. | Speak directly to your conversation partner in your response and address them informally. |
| Detectable Content | No Digits | N'utilisez pas de chiffres arabes dans votre réponse. | Do not use arabic numerals in your response. |


**Main changes in generic instructions:**
- `TitleChecker`: 

  - Original: << title >> 

  - French: ##title##

  Motivation: <<>> is too close to French quotation marks «», and is not really used in French.

- `QuotationChecker`: 
  
  - original: checks for "texte"
  
  - french: checks for «texte» or "texte" or 'texte'
  
  Motivation: all above quotations would be valid in French

  ## Spanish Dataset

  The Spanish specific instructions are:

  | Instruction Group | Instruction | Description| Translation |
  | --- | --- | --- | --- |
  Special Characters | Letter Frequency (ñ) | En tu respuesta, palabras con la letra "ñ" deben aparecer {N} veces. | In your response, words with the letter "ñ" should appear {N} times. |
  Special Characters | Num_words: add words with tildes | Responde con al menos/como máximo {N} palabras con tilde. | Answer with at least / at most {N} words with tildes. |
  Special Characters | Letter Frequency (ü) | En tu respuesta, palabras con la letra "ü" deben aparecer {N} veces. | In your response, words with the letter "ü" should appear {N} times. |
  Punctuation | Interrogation marks | Tu respuesta debe incluir al menos una pregunta. | Your response must express at least one question. |
  Punctuation | Exclamation marks | Tu respuesta debe incluir al menos una exclamación. | Your response must express at least one exclamation. |

