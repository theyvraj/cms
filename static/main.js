document.addEventListener('DOMContentLoaded', function() {
    const footerHtml = `
    <footer class="text-light py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5>Quick Links</h5>
                    <ul class="list-unstyled">
                        <li><a href="/" class="text-light">Home</a></li>
                        <li><a href="/about" class="text-light">About Us</a></li>
                        <li><a href="/contact" class="text-light">Contact Us</a></li>
                        <li><a href="/blogs" class="text-light">Blogs</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Legal</h5>
                    <ul class="list-unstyled">
                        <li><a href="/privacy-policy" class="text-light">Privacy Policy</a></li>
                        <li><a href="/terms-of-service" class="text-light">Terms of Service</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Contact Us</h5>
                    <p>Email: Core@gmail.com</p>
                    <p>Phone: +91 9232311212</p>
                    <p>Address: 82, Mansarovar, Jaipur, Rajasthan</p>
                </div>
            </div>
            <hr class="mt-4">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2025 Core. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <a href="#" class="text-light me-3"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="text-light me-3"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="text-light me-3"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#" class="text-light"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
    </footer>
    `;
    document.body.insertAdjacentHTML('beforeend', footerHtml);
});
