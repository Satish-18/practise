// refrence type

var object1 = { value: 10};
var object2 = object1;
var object3 = { value: 10};

// Context vs scope
const objet4 = {
    a: function() {
        console.log(this);
    }
}

// instantiation
class Player {
    constructor(name, type) {
        console.log('player',this);
        this.name = name;
        this.type = type;
    }
    introduce() {
        console.log(`Hi I am ${this.name}, I'm a ${this.type}`);
    }
}

class wizard extends Player{
    constructor(name, type) {
    super(name, type)
    console.log('wizard', this);
    }
    play() {
        console.log(`WEEEE I'm a ${this.type} `);
    }
}

const wizard1 = new wizard('Shelly', 'Healer');
const wizard2 = new wizard('Satish', 'Unstopable');