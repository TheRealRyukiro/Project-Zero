class Inventory {
	// this function defines the x and y values on the sceen and hight and width
	constructor(Items) {
		this.Items = Items;
		this.sprite = this.Items.Sprite;
		this.rows = Math.ceil(Math.sqrt(this.Items.length));
		this.columns = this.rows;
	}
	// Getters
	getItem(id) {
		return this.Items[id];
	}
	getItemList() {
		return this.Items.join("\n");
	}
	// Setters



	addItem = function additem(Item) {
		this.columns = Math.ceil(Math.sqrt(this.Items.push(Item)));
		this.rows = this.columns
	}
	removeItem = function removeItem(Item) {
		this.Items.splice(Item.ID);
		this.columns = Math.ceil(Math.sqrt(this.Items.length));
		return "Removed " + Item.Name;
	}
	sellItem = function sellItem(Items, Player) {
		if (Array.isArray(Items)) {
			for (item in Items) {
				Player.Money += item.sellValue
				removeItem(item.ID)
			}
		} else if (Items === Item()) {
			Player.Money += Item.sellValue;
		}
	}
}


class Player {
	constructor(Name, Health = 100, Money = 100, Inventory = new Inventory()) {
		this.Name = Name;
		this.Health = Health;
		this.maxHealth = Health;
		this.Money = Money;
		this.characterMade = new Date();
	}
	// Getters
	getName() {
		return this.Name;
	}
	getHealth() {
		return this.Health;
	}
	getMaxHealth() {
		return this.MaxHealth;
	}
	getMoney() {
		return this.Money;
	}

	// Setters
	setMoney() {
		return ++this.Money;
	}
	setHealth(Health) {
		return ++this.Health;
	}
	setMaxHealth(Health) {
		return ++this.MaxHealth;
	}
	setName(Name) {
		return ++this.Name;
	}
	displayHealth() {
		return this.Health.toString() + " / " + this.maxHealth.toString()
	}
	displayMoney() {
		return "$" + this.Money.toString()
	}

}