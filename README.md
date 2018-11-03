# Cabot Cafe Mobile Order

This repo contains the open sourced Mobile-Ordering system for Cabot Cafe at Harvard University. 

The system is optimized for mobile, simplicity, maintainability, and customizability. It is designed for boutique shops with one location with a constantly changing menu / price system.

## Demo

By default when no barista is logged in users are redirected to a "we're closed" page which lists hours.

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/P2.png)

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/V1.png)

When a barista starts a shift they go to `/barista` on safari on the ipad and log in. 

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/P1.png)

After logging in `/barista` then redirects to the dashboard

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/V2.png)

The dashboard will auto-refresh every 5 seconds, checking the order queue database every time. Thus new orders will 'appear' spontaneously on the ipad when placed by customers. When the order is done the barista presses done to clear that order from the database.

When the barista is logged in the home page and tabs will direct to the hot drinks, cold drinks, and food pages instead of redirected to the closed page.

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/V3.png)

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/W1.gif)

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/W2.gif)

To place an order the user taps the buy button and enters their information

![alt text](https://github.com/Radar3699/CabotCafeMobileOrder/blob/master/demos/W3.gif)

## Set Up

### System requirements


System requirements are a [Stripe Account](https://dashboard.stripe.com/register) and 
python3. Stripe is used to process payments and the backend is in python3. 

Python packages are `Flask`, `stripe`, `numpy`, and `SQLalchemy` and can be installed via


```
pip install requirements.txt
```
**Stripe:**
Make sure to obtain a `public key` and `private key` from your Stripe account and fill them in at the top of `app.py`. For testing see [Stripe testing](https://stripe.com/docs/testing#cards), use the test public and private keys , and use the test credit cards.

### Fitting to your business

**Menu:** To set a menu and prices, move `menu_maker.py` from `/helpers` to the main repo. Open `menu_maker.py` and modify the (name,price,image name) triples. image_name should be the name of the image corresponding to the item (in .png or .jpg) in `/static`. Once the menu is set in `menu_maker.py` then run

```
python menu_maker.py
```
which will save your menu as a .json file in the `/menu` folder, and will be accessed by the backend. 

**Barista Login:** Make sure to set the username and password you want in `app.py`.

**Logo:** Look in `/static` and replace `cafe_logo.png` with a small (roughly 100px x 100px) logo and `cafe_logo_big.jpg` with a bigger (roughly 200px x 200px) logo. This will replace all the Cabot cafe logos with your logo. 

**External Links:** Ensure the `Contact / About` div in the header of the html files links to the right place, and the facebook, instagram, and twitter icons in the footer of the html files link to the right places.

**Hours:** Ensure the hours listed in `closed.html` are consistent with your shop. 

## Deployment

We use an ipad that the barista reads from but employees can also use the dashboard via a computer or phone (but need to make sure they won't fall asleep). It's also helpful to print out a piece of paper with login instructions for employees. 

**Testing:** Make sure to test transactions with the Stripe test credit cards for all items before officially launching. 

## Built With

* [Flask](http://flask.pocoo.org/) - The web micro framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database toolkit
* [Stripe](https://stripe.com/) - Used to process payments
* [Numpy](https://github.com/numpy/numpy) - Numerical Computing
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) - Python tenplating engine
* [Bootstrap](https://getbootstrap.com/) - Front end framework used


## Authors

* **Duncan Stothers** - [Follow me](https://github.com/Radar3699)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* *Cabot House* for being wonderful and the greatest house on campus
* *Starbucks Corporation* as a constant source of inspiration

