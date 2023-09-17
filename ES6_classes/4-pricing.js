import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a currency.');
    }
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    this._amount = amount;
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    if (typeof conversionRate !== 'number') {
      throw new TypeError('conversionRate must be a number.');
    }
    return amount * conversionRate;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    this._amount = value;
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError('Currency must be a currency.');
    }
    this._currency = value;
  }

  get currency() {
    return this._currency;
  }
}
