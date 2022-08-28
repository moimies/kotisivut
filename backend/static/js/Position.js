class Position
{
    madeMoves = null;
    letters = null;
    possibleMoves = null;
    x = 0;
    constructor(mm, x_, letters_)
    {
        this.letters = letters_;
        this.x = x_;
        this.madeMoves = JSON.parse(JSON.stringify(mm));
        this.possibleMoves = this.createPossibleDirections();
        if (this.madeMoves.length < 15)
        {
            (this.madeMoves.push(this.x));
        }
    }
    createPossibleDirections()
    {
        var possibles = new Array();
        if (this.x == 0)
        {
            possibles.push(1);
            possibles.push(4);
            possibles.push(5);
        }
        else if (this.x == 1)
        {
            possibles.push(0);
            possibles.push(2);
            possibles.push(4);
            possibles.push(5);
            possibles.push(6);
        }
        else if (this.x == 2)
        {
            possibles.push(1);
            possibles.push(3);
            possibles.push(5);
            possibles.push(6);
            possibles.push(7);
        }
        else if (this.x == 3)
        {
            possibles.push(2);
            possibles.push(6);
            possibles.push(7);
        }
        else if (this.x == 4)
        {
            possibles.push(0);
            possibles.push(1);
            possibles.push(5);
            possibles.push(8);
            possibles.push(9);
        }
        else if (this.x == 5)
        {
            possibles.push(0);
            possibles.push(1);
            possibles.push(2);
            possibles.push(4);
            possibles.push(6);
            possibles.push(8);
            possibles.push(9);
            possibles.push(10);
        }
        else if (this.x == 6)
        {
            possibles.push(1);
            possibles.push(2);
            possibles.push(3);
            possibles.push(5);
            possibles.push(7);
            possibles.push(9);
            possibles.push(10);
            possibles.push(11);
        }
        else if (this.x == 7)
        {
            possibles.push(2);
            possibles.push(3);
            possibles.push(6);
            possibles.push(10);
            possibles.push(11);
        }
        else if (this.x == 8)
        {
            possibles.push(4);
            possibles.push(5);
            possibles.push(9);
            possibles.push(12);
            possibles.push(13);
        }
        else if (this.x == 9)
        {
            possibles.push(4);
            possibles.push(5);
            possibles.push(6);
            possibles.push(8);
            possibles.push(10);
            possibles.push(12);
            possibles.push(13);
            possibles.push(14);
        }
        else if (this.x == 10)
        {
            possibles.push(5);
            possibles.push(6);
            possibles.push(7);
            possibles.push(9);
            possibles.push(11);
            possibles.push(13);
            possibles.push(14);
            possibles.push(15);
        }
        else if (this.x == 11)
        {
            possibles.push(6);
            possibles.push(7);
            possibles.push(10);
            possibles.push(14);
            possibles.push(15);
        }
        else if (this.x == 12)
        {
            possibles.push(8);
            possibles.push(9);
            possibles.push(13);
        }
        else if (this.x == 13)
        {
            possibles.push(8);
            possibles.push(9);
            possibles.push(10);
            possibles.push(12);
            possibles.push(14);
        }
        else if (this.x == 14)
        {
            possibles.push(9);
            possibles.push(10);
            possibles.push(11);
            possibles.push(13);
            possibles.push(15);
        }
        else if (this.x == 15)
        {
            possibles.push(10);
            possibles.push(11);
            possibles.push(14);
        }
        var p = new Array();
        for (let i in possibles) {
            if(this.madeMoves.includes(i)){
                ;
            }else{
                p.push(i);
            }
        }
   
        return p;
    }



    word()
    {
        var w = "";
        for (let i in this.madeMoves) {
        w += this.letters[i];
        return w;
        }
    }
}