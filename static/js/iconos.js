const signos = 
{
    "Mono": "https://www.clarin.com/pages/bundles/horoscopochino/images/mono@2x.png", 
    "Gallo": "https://www.clarin.com/pages/bundles/horoscopochino/images/gallo@2x.png", 
    "Perro": "https://www.clarin.com/pages/bundles/horoscopochino/images/perro@2x.png", 
    "Cerdo": "https://www.clarin.com/pages/bundles/horoscopochino/images/cerdo@2x.png", 
    "Rata": "https://www.clarin.com/pages/bundles/horoscopochino/images/rata@2x.png", 
    "Buey": "https://www.clarin.com/pages/bundles/horoscopochino/images/bufalo@2x.png", 
    "Tigre": "https://www.clarin.com/pages/bundles/horoscopochino/images/tigre@2x.png", 
    "Conejo": "https://www.clarin.com/pages/bundles/horoscopochino/images/conejo@2x.png", 
    "Dragón": "https://www.clarin.com/pages/bundles/horoscopochino/images/dragon@2x.png", 
    "Serpiente": "https://www.clarin.com/pages/bundles/horoscopochino/images/serpiente@2x.png", 
    "Caballo": "https://www.clarin.com/pages/bundles/horoscopochino/images/caballo@2x.png", 
    "Cabra": "https://www.clarin.com/pages/bundles/horoscopochino/images/cabra@2x.png"
};

const colocarIcono = (signo) =>
{
    const imagen = document.getElementById('imgSigno'); 
    imagen.src = signos[signo];
}