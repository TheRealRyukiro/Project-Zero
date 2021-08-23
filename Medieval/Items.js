class Item {
    constructor(Name, ID, Sprite, Description, sellValue = 1, inventoryAmount = 0){
        this.Name = Name;
        this.ID = ID;
        this.Sprite = Sprite;
        this.Description = Description;
        this.sellValue = sellValue;
        this.inventoryAmount = inventoryAmount;
    }
    // Getters
    getName(){ return this.Name; }
    getID(){ return this.ID; }
    getDescription(){ return this.Description; }
    // Setters
    setName(Name){
        let oldName = this.Name;
        this.Name = Name;
        return oldName + " Has been renamed to " + this.Name;
    }
    setID(ID){
        let oldID = this.ID;
        this.ID = ID
        return "ID of " + this.Name + " has changed from | " + oldID + " | to | " + this.ID + " |";
    }
    setDescription(Description){
        let oldDescription = this.Description;
        this.Description = Description;
        return "Description of " + this.Name + " has been changed from \n" + oldDescription + "\n to \n" + this.Description;
    }
    setSprite(Sprite){
        this.Sprite = Sprite;
        return "Sprite Changed to | " + this.Sprite + " |";
    }
    setSellValue(sellValue){
        let oldSellValue = this.sellValue;
        this.sellValue = sellValue;
        return "Sell Price of " + this.Name + " has been changed from | " + oldSellValue + " | to | " + this.sellValue + " |";
         
    }


}