import java.io.BufferedReader;
import java.util.LinkedHashSet;
import java.util.Set;
import java.io.InputStreamReader;
import java.lang.String;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.io.InputStream;


class Etsi {
    #letters;
    words;
    wordsForGame;
    foundWords;

    constructor(letters_) {
        this.words = new Array();
        this.letters = letters_;
        this.wordsForGame = new Array();

        this.initWordList();


    }

    initWordList() {

        addWord = false;
        try {
            InputStream file = this.contxt.getResources().openRawResource(R.raw.words_for_game);
            BufferedReader reader = new BufferedReader(new InputStreamReader(file));

            var reader = new FileReader

            while(reader.ready()) {
                String item = reader.readLine();
                item.replace("\n", "");

                for(char c : item.toCharArray()) {
                    if(!this.letters.contains(c)) {
                        addWord = false;
                        break;
                    }else {
                        addWord = true;
                    }
                }

                if(item.length() > 16) {
                    addWord = false;
                    ;
                }
                if(addWord) {
                    this.wordsForGame.add(item);
                }
            }
            reader.close();
            //System.out.println("WORDS FOR GAME AMOUnT: " + this.wordsForGame.size());


            this.findWords();
        }catch (Exception e) {
            //System.out.println("Error");
            //System.out.println(System.getProperty("user.dir"));
            e.printStackTrace();
        }

    }

    ArrayList<String> listforPos(Position p, ArrayList<String> wordlist){
        ArrayList<String> list = new ArrayList<String>();

        int pituus = p.madeMoves.size();

        for(String s : wordlist) {


            if(s.toLowerCase().equals(p.word().toLowerCase())){
                this.words.add(s);
            }else if(s.substring(0, pituus).toLowerCase().equals(p.word().toLowerCase())) {
                list.add(s);
            }
        }

        return list;

    }

    private void call(Position p, ArrayList<String> wordstoparse) {
        ArrayList<Integer> possibles = p.possibleMoves;

        for(Integer i : possibles) {
            Position temp = new Position(p.madeMoves, i , this.letters);
            //System.out.println(temp.word());
            ArrayList<String> l = this.listforPos(temp, wordstoparse);

            if(l.size() != 0) {
                this.call(temp, l);
            }
        }

    }

    void findWords(){
        for(int x = 0; x < letters.size(); x++) {
            this.call(new Position(new ArrayList<Integer>(), x, letters), this.wordsForGame);
        }


        Collections.sort(this.words, new Comparator<String>() {
            public int compare(String o1, String o2){

                return o1.length() - o2.length();
            }
        });

        Collections.reverse(this.words);


        Set<String> set = new LinkedHashSet<>(this.words);

        this.words.clear();
        this.words.addAll(set);

        for(String s : this.words) {
            //System.out.println(s);
        }

        //System.out.println("Len of words found: " + this.words.size());
    }




}

