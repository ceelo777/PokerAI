import React from 'react';

import Card from './Card';

export default function Hand(props) {
    const {showCard, cards} = props.data

    const cardsList = cards.map((card, index) => {
        return <Card key={"card"+index} className="cards" data={{
            showCard: showCard,
            value: card
        }} />
    })

    return (
        <div className="Hand">
            {cardsList}
        </div>
    )
}