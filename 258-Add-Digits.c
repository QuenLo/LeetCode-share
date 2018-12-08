int addDigits(int num) {
    int result = num % 9;
    return (result != 0 || num == 0 ) ? result : 9;
}
