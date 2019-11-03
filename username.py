'''
# データ型宣言
# 属性
#  実際のユーザ名
- ルール
- ユーザ名は4文字以上,20文字以内であること => メソッド
- ユーザ名を大文字に変換する
'''


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}は文字数のルール違反やで!")
        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化
hibiki = UserName(name="hibiki")
print(hibiki.screen_name())
# print(type(hibiki))
# print(hibiki)
# print(hibiki.name)

# shota = UserName('shota')
# print(sho.name)
