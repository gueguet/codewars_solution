// https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/javascript

function declareWinner(fighter1, fighter2, firstAttacker) {
    
    while(fighter1.health > 0 || fighter2.health > 0) {

        if (fighter1.name === firstAttacker) {
            fighter2.health -= fighter1.damagePerAttack
            if (fighter2.health <= 0) {
                return fighter1.name
            }
            else {
                fighter1.health -= fighter2.damagePerAttack;
            }
        }

        else {
            fighter1.health -= fighter2.damagePerAttack
            if (fighter1.health <= 0) {
                return fighter2.name
            }
            else {
                fighter2.health -= fighter1.damagePerAttack;
            }
        }

        if (fighter1.health <= 0) {
            return fighter2.name
        }

        if (fighter2.health <= 0) {
            return fighter1.name
        }

    }
    
    return "Write your code here";
}



/* clever

function declareWinner(fighter1, fighter2, firstAttacker) {
  while (fighter1.health > 0 && fighter2.health > 0) {
    fighter2.health -= fighter1.damagePerAttack;
    fighter1.health -= fighter2.damagePerAttack;
  }
  
  if (fighter1.health <= 0 && fighter2.health <= 0)
    return firstAttacker;
  else if (fighter1.health <= 0)
    return fighter2.name;
  else
    return fighter1.name;
}

------------------------------------------------------------------

function declareWinner(fighter1, fighter2, firstAttacker) {
  var fac1 = Math.ceil( fighter1.health / fighter2.damagePerAttack );
  var fac2 = Math.ceil( fighter2.health / fighter1.damagePerAttack );
  if(fac1 < fac2) {
    return fighter2.name;
  } else if(fac2 < fac1) {
    return fighter1.name;
  } else {
    return firstAttacker;
  }
}


*/

