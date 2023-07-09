package ComplexNumber;

class Complex {
    public float real;
    public float imaginary;

    Complex(float real, float imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public Complex add(Complex other) {
        return new Complex( real + other.real, imaginary + other.imaginary );
    }

    public Complex add( float real, float imaginary) {

        this.real += real;
        this.imaginary += imaginary;

        return this;
    }
}