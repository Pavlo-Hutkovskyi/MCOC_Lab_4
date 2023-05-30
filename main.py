import statistics
import numpy as np
import matplotlib.pyplot as plot


def errorCalculating(approximate, accurate):
    absolute, relative = np.abs(approximate - accurate), np.abs(approximate - accurate) / np.abs(accurate) * 100
    return np.max(absolute), np.min(absolute), np.max(relative), np.min(relative)


def harmonicMean(valuesArray):
    return len(valuesArray) / np.sum(1 / np.abs(valuesArray))


def geometricMean(valuesArray):
    specificValues = [(value if value >= 0 else np.abs(value)) for value in valuesArray]
    return statistics.geometric_mean(specificValues)


def arithmeticMean(valuesArray):
    return np.mean(valuesArray)


def showGraphic(x, approximate, accurate):
    plot.title("N = " + str(N))
    # plot.plot(x, [approximateArithmetic] * len(x), label='- середнє арифметичне', color="green")
    # plot.plot(x, [approximateGeometric] * len(x), label='- середнє гармонічне', color="purple")
    # plot.plot(x, [approximateHarmonic] * len(x), label='- середнє геометричне', color="yellow")
    plot.plot(x, approximate, label='- наближена функція', color="blue")
    plot.plot(x, accurate, label='- точна функція', color="red", linewidth=2)
    plot.xlabel('x')
    plot.ylabel('y')
    plot.legend()
    plot.show()


def showResult():
    for i in range(3):
        print("Наближене середнє " + names[i] + "е:\t" + str(dataMeans[i][0]))
        print("Точне середнє " + names[i] + "е:\t\t" + str(dataMeans[i][1]), end="\n\n")


n = 5
N, A, phi, error = 1000 * n, 1.0, np.pi / 4, 0.05
x = np.linspace(0, 1, N)
noise = np.random.uniform(-error * A, error * A, N)
yApproximate, yAccurate = A * np.sin(n * x + phi) + noise + n, A * np.sin(n * x + phi) + n
names = ["арифметичн", "гармонічн", "геометричн"]
dataMeans = []

approximateArithmetic, accurateArithmetic = arithmeticMean(yApproximate), arithmeticMean(yAccurate)
dataMeans.append([approximateArithmetic, accurateArithmetic])

approximateHarmonic, accurateHarmonic = harmonicMean(yApproximate), harmonicMean(yAccurate)
dataMeans.append([approximateHarmonic, accurateHarmonic])

approximateGeometric, accurateGeometric = geometricMean(yApproximate), geometricMean(yAccurate)
dataMeans.append([approximateGeometric, accurateGeometric])

maxAbsolute, minAbsolute, maxRelative, minRelative = errorCalculating(yApproximate, yAccurate)

showGraphic(x, yApproximate, yAccurate)
showResult()


print(f"Абсолютна максимальна похибка:\t {maxAbsolute}")
print(f"Абсолютна мінімальна похибка:\t {minAbsolute}")
print(f"Відносна максимальна похибка:\t {maxRelative / (N / n)}")
print(f"Відносна мінімальна похибка:\t {minRelative}")

