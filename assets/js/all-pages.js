/*

Co vše se zde bude řešit:
- bookmark - načtení z LS, vytvoření nového, správa (možnost změny barvy nebo ikony)
- vzhled: klasický || růžový
- místa - vlastní rozsah
- připnout cvik nahoru

- import export local storage value

- zobrazení tůry


*/



function extendObj(obj1, obj2, overwrite) {
  Object.keys(obj2).forEach(function (key) {
    if (!obj1.hasOwnProperty(key) || overwrite) {
      obj1[key] = obj2[key];
    }
  })
}



var bookmarkIcon = document.getElementById('bookmark-icon');
if (bookmarkIcon) {
  bookmarkIcon.addEventListener('click', function () {
    console.log("bookmark click");
  });
}



function Page() {
  // reprezentuje stránku

}

extendObj(Page.prototype, {
  runAfterLoad: function () {
    console.log('TODO: load bookmarks from localStorage');
    console.log('TODO: set nav links active based on url adress');
  }
});


var page = new Page();

window.addEventListener('DOMContentLoaded', function (event) {
  page.runAfterLoad();
});



// Kalkulačky

var Kalk = (function () {

  var BasalMetablicRate = function () {
    // Vrozce pro výpočet BMR + konstany podle aktivity
    function vzorec(konst, k_vaha, k_vyska, k_vek) {
      // podle kostant vrátí funkce pro vzorce
      return function (vaha, vyska, vek) {
        return konst + (k_vaha * vaha) + (k_vyska * vyska) - (k_vek * vek);
      }
    }

    return {
      Z: vzorec(655.0955, 9.5634, 1.8496, 4.6756),
      M: vzorec(66.473, 13.7516, 5.0033, 6.755),
      aktivita: {
        1: {konst: 1.2,   popis: "Žádný aktivní pohyb"},
        2: {konst: 1.375, popis: "Sport 1-3x týdně"},
        3: {konst: 1.55,  popis: "Sport 3-5x týdně"},
        4: {konst: 1.725, popis: "Sport 6-7x týdně"},
        5: {konst: 1.9},  popis: "Extrém: 2 fázové tréningy"
      },
      J: 'kcal'
    }
  };

  return {
    BMR: BasalMetablicRate()
  }
})();