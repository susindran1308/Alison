import startPage
import AlisonInterface

if __name__ == '__main__':
    language = startPage.main()
    alison = AlisonInterface.Interface(language).main()
