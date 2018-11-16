import requests
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/boxscores/"

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content,"html.parser")
for td in soup.find_all('td')[1]:
    trs = soup.find_all('tr')
    # print("-%s - %s - %s - %s - %s - %s\n" % \
    # (trs[0].text, trs[1].text, trs[2].text, trs[3].text, trs[4].text, trs[5].text))

################################################################################

nscore_1 = trs[0].text
nscore_1 = nscore_1.strip('\n')
nscore_1 = nscore_1.strip('\t')
nscore_1 = nscore_1.replace('\n',' ')
nscore_1 = nscore_1.replace('\t',' ')
nscore_2 = trs[1].text
nscore_2 = nscore_2.strip('\n')
nscore_2 = nscore_2.strip('\t')
nscore_2 = nscore_2.replace('\n',' ')
nscore_2 = nscore_2.replace('\t',' ')
nscore_3 = trs[5].text
nscore_3 = nscore_3.strip('\n')
nscore_3 = nscore_3.strip('\t')
nscore_3 = nscore_3.replace('\n',' ')
nscore_3 = nscore_3.replace('\t',' ')
nscore_4 = trs[6].text
nscore_4 = nscore_4.strip('\n')
nscore_4 = nscore_4.strip('\t')
nscore_4 = nscore_4.replace('\n',' ')
nscore_4 = nscore_4.replace('\t',' ')

index1 = nscore_1.find("Division")
index2 = nscore_2.find("Division")
index3 = nscore_3.find("Division")
index4 = nscore_4.find("Division")
if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
    game1a = nscore_1
    game1b = nscore_2
    game1c = nscore_3
    game1d = nscore_4

## then search for game 2
    nscore_1 = trs[7].text
    nscore_1 = nscore_1.strip('\n')
    nscore_1 = nscore_1.strip('\t')
    nscore_1 = nscore_1.replace('\n',' ')
    nscore_1 = nscore_1.replace('\t',' ')
    nscore_2 = trs[8].text
    nscore_2 = nscore_2.strip('\n')
    nscore_2 = nscore_2.strip('\t')
    nscore_2 = nscore_2.replace('\n',' ')
    nscore_2 = nscore_2.replace('\t',' ')
    nscore_3 = trs[12].text
    nscore_3 = nscore_3.strip('\n')
    nscore_3 = nscore_3.strip('\t')
    nscore_3 = nscore_3.replace('\n',' ')
    nscore_3 = nscore_3.replace('\t',' ')
    nscore_4 = trs[13].text
    nscore_4 = nscore_4.strip('\n')
    nscore_4 = nscore_4.strip('\t')
    nscore_4 = nscore_4.replace('\n',' ')
    nscore_4 = nscore_4.replace('\t',' ')
    index1 = nscore_1.find("Division")
    index2 = nscore_2.find("Division")
    index3 = nscore_3.find("Division")
    index4 = nscore_4.find("Division")

    if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
        game2a = nscore_1
        game2b = nscore_2
        game2c = nscore_3
        game2d = nscore_4

        # Search for Game 3
        nscore_1 = trs[14].text
        nscore_1 = nscore_1.strip('\n')
        nscore_1 = nscore_1.strip('\t')
        nscore_1 = nscore_1.replace('\n',' ')
        nscore_1 = nscore_1.replace('\t',' ')
        nscore_2 = trs[15].text
        nscore_2 = nscore_2.strip('\n')
        nscore_2 = nscore_2.strip('\t')
        nscore_2 = nscore_2.replace('\n',' ')
        scor10 = nscore_2.replace('\t',' ')
        nscore_3 = trs[19].text
        nscore_3 = nscore_3.strip('\n')
        nscore_3 = nscore_3.strip('\t')
        nscore_3 = nscore_3.replace('\n',' ')
        nscore_3 = nscore_3.replace('\t',' ')
        nscore_4 = trs[20].text
        nscore_4 = nscore_4.strip('\n')
        nscore_4 = nscore_4.strip('\t')
        nscore_4 = nscore_4.replace('\n',' ')
        nscore_4 = nscore_4.replace('\t',' ')
        index1 = nscore_1.find("Division")
        index2 = nscore_2.find("Division")
        index3 = nscore_3.find("Division")
        index4 = nscore_4.find("Division")
        if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
            game3a = nscore_1
            game3b = nscore_2
            game3c = nscore_3
            game3d = nscore_4

            # Search for Game 4
            nscore_1 = trs[21].text
            nscore_1 = nscore_1.strip('\n')
            nscore_1 = nscore_1.strip('\t')
            nscore_1 = nscore_1.replace('\n',' ')
            nscore_1 = nscore_1.replace('\t',' ')
            nscore_2 = trs[22].text
            nscore_2 = nscore_2.strip('\n')
            nscore_2 = nscore_2.strip('\t')
            nscore_2 = nscore_2.replace('\n',' ')
            nscore_2 = nscore_2.replace('\t',' ')
            nscore_3 = trs[26].text
            nscore_3 = nscore_3.strip('\n')
            nscore_3 = nscore_3.strip('\t')
            nscore_3 = nscore_3.replace('\n',' ')
            nscore_3 = nscore_3.replace('\t',' ')
            nscore_4 = trs[27].text
            nscore_4 = nscore_4.strip('\n')
            nscore_4 = nscore_4.strip('\t')
            nscore_4 = nscore_4.replace('\n',' ')
            nscore_4 = nscore_4.replace('\t',' ')
            index1 = nscore_1.find("Division")
            index2 = nscore_2.find("Division")
            index3 = nscore_3.find("Division")
            index4 = nscore_4.find("Division")
            if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                game4a = nscore_1
                game4b = nscore_2
                game4c = nscore_3
                game4d = nscore_4

                # Search for game 5
                nscore_1 = trs[28].text
                nscore_1 = nscore_1.strip('\n')
                nscore_1 = nscore_1.strip('\t')
                nscore_1 = nscore_1.replace('\n',' ')
                nscore_1 = nscore_1.replace('\t',' ')
                nscore_2 = trs[29].text
                nscore_2 = nscore_2.strip('\n')
                nscore_2 = nscore_2.strip('\t')
                nscore_2 = nscore_2.replace('\n',' ')
                nscore_2 = nscore_2.replace('\t',' ')
                nscore_3 = trs[33].text
                nscore_3 = nscore_3.strip('\n')
                nscore_3 = nscore_3.strip('\t')
                nscore_3 = nscore_3.replace('\n',' ')
                nscore_3 = nscore_3.replace('\t',' ')
                nscore_4 = trs[34].text
                nscore_4 = nscore_4.strip('\n')
                nscore_4 = nscore_4.strip('\t')
                nscore_4 = nscore_4.replace('\n',' ')
                nscore_4 = nscore_4.replace('\t',' ')
                index1 = nscore_1.find("Division")
                index2 = nscore_2.find("Division")
                index3 = nscore_3.find("Division")
                index4 = nscore_4.find("Division")
                if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-20:
                    game5a = nscore_1
                    game5b = nscore_2
                    game5c = nscore_3
                    game5d = nscore_4

                    # Search for game 6
                    nscore_1 = trs[35].text
                    nscore_1 = nscore_1.strip('\n')
                    nscore_1 = nscore_1.strip('\t')
                    nscore_1 = nscore_1.replace('\n',' ')
                    nscore_1 = nscore_1.replace('\t',' ')
                    nscore_2 = trs[36].text
                    nscore_2 = nscore_2.strip('\n')
                    nscore_2 = nscore_2.strip('\t')
                    nscore_2 = nscore_2.replace('\n',' ')
                    nscore_2 = nscore_2.replace('\t',' ')
                    nscore_3 = trs[40].text
                    nscore_3 = nscore_3.strip('\n')
                    nscore_3 = nscore_3.strip('\t')
                    nscore_3 = nscore_3.replace('\n',' ')
                    nscore_3 = nscore_3.replace('\t',' ')
                    nscore_4 = trs[41].text
                    nscore_4 = nscore_4.strip('\n')
                    nscore_4 = nscore_4.strip('\t')
                    nscore_4 = nscore_4.replace('\n',' ')
                    nscore_4 = nscore_4.replace('\t',' ')
                    index1 = nscore_1.find("Division")
                    index2 = nscore_2.find("Division")
                    index3 = nscore_3.find("Division")
                    index4 = nscore_4.find("Division")
                    if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                        game6a = nscore_1
                        game6b = nscore_2
                        game6c = nscore_3
                        game6d = nscore_4

                        # Search for game 7
                        nscore_1 = trs[42].text
                        nscore_1 = nscore_1.strip('\n')
                        nscore_1 = nscore_1.strip('\t')
                        nscore_1 = nscore_1.replace('\n',' ')
                        nscore_1 = nscore_1.replace('\t',' ')
                        nscore_2 = trs[43].text
                        nscore_2 = nscore_2.strip('\n')
                        nscore_2 = nscore_2.strip('\t')
                        nscore_2 = nscore_2.replace('\n',' ')
                        nscore_2 = nscore_2.replace('\t',' ')
                        nscore_3 = trs[47].text
                        nscore_3 = nscore_3.strip('\n')
                        nscore_3 = nscore_3.strip('\t')
                        nscore_3 = nscore_3.replace('\n',' ')
                        nscore_3 = nscore_3.replace('\t',' ')
                        nscore_4 = trs[48].text
                        nscore_4 = nscore_4.strip('\n')
                        nscore_4 = nscore_4.strip('\t')
                        nscore_4 = nscore_4.replace('\n',' ')
                        nscore_4 = nscore_4.replace('\t',' ')
                        index1 = nscore_1.find("Division")
                        index2 = nscore_2.find("Division")
                        index3 = nscore_3.find("Division")
                        index4 = nscore_4.find("Division")
                        if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                            game7a = nscore_1
                            game7b = nscore_2
                            game7c = nscore_3
                            game7d = nscore_4

                            # search for game 8
                            nscore_1 = trs[49].text
                            nscore_1 = nscore_1.strip('\n')
                            nscore_1 = nscore_1.strip('\t')
                            nscore_1 = nscore_1.replace('\n',' ')
                            nscore_1 = nscore_1.replace('\t',' ')
                            nscore_2 = trs[50].text
                            nscore_2 = nscore_2.strip('\n')
                            nscore_2 = nscore_2.strip('\t')
                            nscore_2 = nscore_2.replace('\n',' ')
                            nscore_2 = nscore_2.replace('\t',' ')
                            nscore_3 = trs[54].text
                            nscore_3 = nscore_3.strip('\n')
                            nscore_3 = nscore_3.strip('\t')
                            nscore_3 = nscore_3.replace('\n',' ')
                            nscore_3 = nscore_3.replace('\t',' ')
                            nscore_4 = trs[55].text
                            nscore_4 = nscore_4.strip('\n')
                            nscore_4 = nscore_4.strip('\t')
                            nscore_4 = nscore_4.replace('\n',' ')
                            nscore_4 = nscore_4.replace('\t',' ')
                            index1 = nscore_1.find("Division")
                            index2 = nscore_2.find("Division")
                            index3 = nscore_3.find("Division")
                            index4 = nscore_4.find("Division")
                            if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                                game8a = nscore_1
                                game8b = nscore_2
                                game8c = nscore_3
                                game8d = nscore_4

                                # search for game 9
                                nscore_1 = trs[56].text
                                nscore_1 = nscore_1.strip('\n')
                                nscore_1 = nscore_1.strip('\t')
                                nscore_1 = nscore_1.replace('\n',' ')
                                nscore_1 = nscore_1.replace('\t',' ')
                                nscore_2 = trs[57].text
                                nscore_2 = nscore_2.strip('\n')
                                nscore_2 = nscore_2.strip('\t')
                                nscore_2 = nscore_2.replace('\n',' ')
                                nscore_2 = nscore_2.replace('\t',' ')
                                nscore_3 = trs[61].text
                                nscore_3 = nscore_3.strip('\n')
                                nscore_3 = nscore_3.strip('\t')
                                nscore_3 = nscore_3.replace('\n',' ')
                                nscore_3 = nscore_3.replace('\t',' ')
                                nscore_4 = trs[62].text
                                nscore_4 = nscore_4.strip('\n')
                                nscore_4 = nscore_4.strip('\t')
                                nscore_4 = nscore_4.replace('\n',' ')
                                nscore_4 = nscore_4.replace('\t',' ')
                                index1 = nscore_1.find("Division")
                                index2 = nscore_2.find("Division")
                                index3 = nscore_3.find("Division")
                                index4 = nscore_4.find("Division")
                                if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                                    game9a = nscore_1
                                    game9b = nscore_2
                                    game9c = nscore_3
                                    game9d = nscore_4

                                    # Search for game 10
                                    nscore_1 = trs[63].text
                                    nscore_1 = nscore_1.strip('\n')
                                    nscore_1 = nscore_1.strip('\t')
                                    nscore_1 = nscore_1.replace('\n',' ')
                                    nscore_1 = nscore_1.replace('\t',' ')
                                    nscore_2 = trs[64].text
                                    nscore_2 = nscore_2.strip('\n')
                                    nscore_2 = nscore_2.strip('\t')
                                    nscore_2 = nscore_2.replace('\n',' ')
                                    nscore_2 = nscore_2.replace('\t',' ')
                                    nscore_3 = trs[68].text
                                    nscore_3 = nscore_3.strip('\n')
                                    nscore_3 = nscore_3.strip('\t')
                                    nscore_3 = nscore_3.replace('\n',' ')
                                    nscore_3 = nscore_3.replace('\t',' ')
                                    nscore_4 = trs[69].text
                                    nscore_4 = nscore_4.strip('\n')
                                    nscore_4 = nscore_4.strip('\t')
                                    nscore_4 = nscore_4.replace('\n',' ')
                                    nscore_4 = nscore_4.replace('\t',' ')
                                    index1 = nscore_1.find("Division")
                                    index2 = nscore_2.find("Division")
                                    index3 = nscore_3.find("Division")
                                    index4 = nscore_4.find("Division")
                                    if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                                        game10a = nscore_1
                                        game10b = nscore_2
                                        game10c = nscore_3
                                        game10d = nscore_4

                                        # Search for game 11
                                        nscore_1 = trs[70].text
                                        nscore_1 = nscore_1.strip('\n')
                                        nscore_1 = nscore_1.strip('\t')
                                        nscore_1 = nscore_1.replace('\n',' ')
                                        nscore_1 = nscore_1.replace('\t',' ')
                                        nscore_2 = trs[71].text
                                        nscore_2 = nscore_2.strip('\n')
                                        nscore_2 = nscore_2.strip('\t')
                                        nscore_2 = nscore_2.replace('\n',' ')
                                        nscore_2 = nscore_2.replace('\t',' ')
                                        nscore_3 = trs[75].text
                                        nscore_3 = nscore_3.strip('\n')
                                        nscore_3 = nscore_3.strip('\t')
                                        nscore_3 = nscore_3.replace('\n',' ')
                                        nscore_3 = nscore_3.replace('\t',' ')
                                        nscore_4 = trs[76].text
                                        nscore_4 = nscore_4.strip('\n')
                                        nscore_4 = nscore_4.strip('\t')
                                        nscore_4 = nscore_4.replace('\n',' ')
                                        nscore_4 = nscore_4.replace('\t',' ')
                                        index1 = nscore_1.find("Division")
                                        index2 = nscore_2.find("Division")
                                        index3 = nscore_3.find("Division")
                                        index4 = nscore_4.find("Division")
                                        if index1 == -1 and index2 == -1 and index3 == -1 and index4 ==-1:
                                            game11a = nscore_1
                                            game11b = nscore_2
                                            game11c = nscore_3
                                            game11d = nscore_4

                                            # if all eleven games print all
                                            print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                                            print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                                            print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                                            print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                                            print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                                            print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                                            print("--------\nGAME 7 \n{} \n{} \n{} \n{} \n--------\n".format(game7a,game7b,game7c,game7d))
                                            print("--------\nGAME 8 \n{} \n{} \n{} \n{} \n--------\n".format(game8a,game8b,game8c,game8d))
                                            print("--------\nGAME 9 \n{} \n{} \n{} \n{} \n--------\n".format(game9a,game9b,game9c,game9d))
                                            print("--------\nGAME 10 \n{} \n{} \n{} \n{} \n--------\n".format(game10a,game10b,game10c,game10d))
                                            print("--------\nGAME 11 \n{} \n{} \n{} \n{} \n--------\n".format(game11a,game11b,game11c,game11d))


                                        else:
                                            # if no eleventh game, print games 1-10
                                            print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                                            print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                                            print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                                            print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                                            print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                                            print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                                            print("--------\nGAME 7 \n{} \n{} \n{} \n{} \n--------\n".format(game7a,game7b,game7c,game7d))
                                            print("--------\nGAME 8 \n{} \n{} \n{} \n{} \n--------\n".format(game8a,game8b,game8c,game8d))
                                            print("--------\nGAME 9 \n{} \n{} \n{} \n{} \n--------\n".format(game9a,game9b,game9c,game9d))
                                            print("--------\nGAME 10 \n{} \n{} \n{} \n{} \n--------\n".format(game10a,game10b,game10c,game10d))
                                    else:
                                        # if no tenth game, print games 1-9
                                        print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                                        print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                                        print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                                        print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                                        print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                                        print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                                        print("--------\nGAME 7 \n{} \n{} \n{} \n{} \n--------\n".format(game7a,game7b,game7c,game7d))
                                        print("--------\nGAME 8 \n{} \n{} \n{} \n{} \n--------\n".format(game8a,game8b,game8c,game8d))
                                        print("--------\nGAME 9 \n{} \n{} \n{} \n{} \n--------\n".format(game9a,game9b,game9c,game9d))
                                else:
                                    # if no ninth game, print only games 1-8
                                    print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                                    print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                                    print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                                    print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                                    print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                                    print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                                    print("--------\nGAME 7 \n{} \n{} \n{} \n{} \n--------\n".format(game7a,game7b,game7c,game7d))
                                    print("--------\nGAME 8 \n{} \n{} \n{} \n{} \n--------\n".format(game8a,game8b,game8c,game8d))

                            else:
                                # if no eight game, print only games 1-7
                                print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                                print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                                print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                                print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                                print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                                print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                                print("--------\nGAME 7 \n{} \n{} \n{} \n{} \n--------\n".format(game7a,game7b,game7c,game7d))
                        else:
                            # if no seventh game, print only games 1-6
                            print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                            print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                            print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                            print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                            print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))
                            print("--------\nGAME 6 \n{} \n{} \n{} \n{} \n--------\n".format(game6a,game6b,game6c,game6d))
                    else:
                        # if no sixth game, print only games 1-5
                        print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                        print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                        print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                        print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
                        print("--------\nGAME 5 \n{} \n{} \n{} \n{} \n--------\n".format(game5a,game5b,game5c,game5d))

                else:
                    # if no fifth game, print only games 1 2 3 4
                    print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                    print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                    print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
                    print("--------\nGAME 4 \n{} \n{} \n{} \n{} \n--------\n".format(game4a,game4b,game4c,game4d))
            else:
                # if no fourth game, print only games 1 2 3
                print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
                print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
                print("--------\nGAME 3 \n{} \n{} \n{} \n{} \n--------\n".format(game3a,game3b,game3c,game3d))
        else:
            # if no third game, print only games 1 and 2
            print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
            print("--------\nGAME 2 \n{} \n{} \n{} \n{} \n--------\n".format(game2a,game2b,game2c,game2d))
    else:
        # if no second game, print only game 1
        print("--------\nGAME 1 \n{} \n{} \n{} \n{} \n--------\n".format(game1a,game1b,game1c,game1d))
else:
    print("There were no NBA games played yesterday")