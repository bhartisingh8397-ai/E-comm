from flask import Flask
from models import db, Product, User
from werkzeug.security import generate_password_hash

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce_v2.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def seed_db():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Add sample products (Total 15)
        products = [
            Product(name='Jahnvi Chrono Z1', price=599.99, description='Ultra-premium luxury smartwatch with glass casing.', image_url='static/images/watch.png', category='Wearables', size='Standard', is_available=True),
            Product(name='Neon Sound S5', price=349.99, description='Futuristic noise-canceling headphones.', image_url='static/images/headphones.png', category='Audio', size='One Size', is_available=True),
            Product(name='Spectre Elite X', price=1899.99, description='Ultra-thin luxury laptop, matte space grey.', image_url='static/images/laptop.png', category='Computers', size='14-inch', is_available=True),
            Product(name='Lumina Desk Lamp', price=129.99, description='Minimalist LED desk lamp with touch controls.', image_url='static/images/lamp.png', category='Home', size='Medium', is_available=True),
            Product(name='Sonic Wave Speaker', price=249.99, description='High-fidelity Bluetooth speaker with 360 sound.', image_url='static/images/speaker.png', category='Audio', size='Portable', is_available=False),
            Product(name='Vision VR Headset', price=799.99, description='Next-gen VR goggles for immersive experiences.', image_url='static/images/vr.png', category='Wearables', size='Adjustable', is_available=True),
            Product(name='Titan Mech Keyboard', price=199.99, description='Premium mechanical keyboard with gold switches.', image_url='static/images/keyboard.png', category='Computers', size='Full Size', is_available=True),
            Product(name='Aether Mouse Pad', price=49.99, description='Luxury microfiber mouse pad with gold stitching.', image_url='static/images/mousepad.png', category='Accessories', size='XL', is_available=True),
            Product(name='Nebula Tablet S1', price=649.99, description='Ultra-thin tablet with vibrant OLED display.', image_url='static/images/tablet.png', category='Computers', size='11-inch', is_available=True),
            Product(name='Rose Gold Silk Dress', price=299.99, description='Premium evening gown with an elegant, glowing finish.', image_url='static/images/dress.png', category='Clothes', size='Medium', is_available=True),
            Product(name='Midnight Leather Jacket', price=499.99, description='Designer black leather jacket for modern aesthetics.', image_url='static/images/jacket.png', category='Clothes', size='Large', is_available=True),
            Product(name='Cashmere Winter Scarf', price=149.99, description='Luxury cashmere scarf featuring subtle patterns.', image_url='static/images/scarf.png', category='Clothes', size='One Size', is_available=True),
            Product(name='Eternity Diamond Necklace', price=1299.99, description='Stunning diamond and gold pendant masterpiece.', image_url='static/images/necklace.png', category='Jewelry', size='18-inch', is_available=True),
            Product(name='Solitaire Platinum Ring', price=2499.99, description='Flawless solitaire diamond engagement ring.', image_url='static/images/ring.png', category='Jewelry', size='Size 7', is_available=False),
            Product(name='Jahnvi Pearl Drop Earrings', price=899.99, description='Elegant pearl and premium gold drop earrings.', image_url='static/images/earrings.png', category='Jewelry', size='Standard', is_available=True)
        ]
        
        # Clear existing data and add 15 products
        db.session.query(Product).delete()
        for p in products:
            db.session.add(p)
            
        # Add a test user with modern hashing
        existing_user = User.query.filter_by(email='test@example.com').first()
        if existing_user:
            db.session.delete(existing_user)
            
        test_user = User(
            email='test@example.com', 
            name='Test User', 
            # Default scrypt hashing for compatibility
            password=generate_password_hash('password123')
        )
        db.session.add(test_user)
            
        db.session.commit()
        print("Database re-seeded successfully with modern hashing!")

if __name__ == '__main__':
    seed_db()
