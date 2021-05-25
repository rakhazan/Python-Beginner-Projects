# Mad Libs project

# # overview
# Mad Libs are a fun way to tell story
# The story is pre-written except for a few missing words
# The story is hidden from the user
# The user is asked a series of questions in oeder to fill in missing words before seeing the story
# Then the story is read off with the user's words mixed in !

country = input("Enter country : ")
name = input("Enter name : ")
insiden = input("Enter insiden : ")
rutin = input("Enter rutine : ")
feel = input("Enter feeling : ")
bawaan = input("Enter bawaan : ")
cara = input("Enter cara menuju suatu lokasi : ")

print("""==================================================
A Day in {}: a Mad Lib.
Welcome! You are about to play a fantastic word game.
I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
Using those words I will create an unexpected story for you!
==================================================""".format(country))

print(f"""
Pagi hari disebuah kota terdapat seorang anak yang bernama {name}, {name} sering membuat masalah. Sebenarnya dia adalah anak yang baik namun beberapa tahun yang lalu ayah dan ibunya meninggal dalam sebuah insiden {insiden}.

Hampir setiap hari dia membuat {rutin} di kota tersebut sampai sampai warga sekitar sudah hafal apa yang akan dilakukannya sekarang dan esok harinya. Para wargapun mengerti kenapa dia melakukan hal tersebut.

Sampai suatu ketika dipagi hari {name} tidak muncul dan membuat masalah seperti biasanya, pada saat itu bukannya {feel} para warga yang biasa dibuat repot oleh {name} ini pun bingung dan merasa khawatir terhadap {name}.

Setelah salah seorang warga yang dimana adalah tetangga dari {name} memberi tahu bahwa {name} sedang sakit dan terbaring dikasur. Sontak warga lainnya pun merasa {feel} dan tanpa pikir panjang mereka menghentikan kegiatan mereka pada saat itu, lalu bersama-sama {cara} menuju rumahnya {name} dengan membawa berbagai macam {bawaan}.
""")