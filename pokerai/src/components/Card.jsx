import React, {useState} from 'react';

// Define file-wide constants
const cardback = require("../img/cardback.svg");
const cardDir = "img/cards/";
const cardSuits = {
    c: 'clubs',
    d: 'diamonds',
    s: 'spades',
    h: 'hearts'
}

export default function Card(props) {
    const [isShow, setIsShow] = useState(props.showCard);

    function toggleShow() {
        setIsShow(!isShow);
    }

    const card = props.data.value;
    const cardValue = card.substring(0, 1)
    const cardSuit = cardSuits[card.substring(1, )];
    if (cardSuit === undefined) {
        console.log("This is not a real suit...");
        // TODO: do something else to check
    }
    const card_file = cardDir + cardValue + "_" + cardSuit + ".svg";
    return (
        <div>
            { isShow 
                ? <img src={require("../" + card_file)} 
                        alt={card_file} 
                        onClick={toggleShow}
                        className="card"></img>
                : <img src={cardback} 
                        alt="opponent card" 
                        onClick={toggleShow}
                        className="card"></img>
            }
        </div>
    );
}
