# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


Console.Clear();

Console.Write("Введите коодинаты xA: ");
//string xyA = Console.ReadLine()!;
double xA = double.Parse(Console.ReadLine()!);
Console.Write("Введите коодинаты yA: ");
double yA = double.Parse(Console.ReadLine()!);

Console.Write("Введите коодинаты xB: ");
double xB = double.Parse(Console.ReadLine()!);
Console.Write("Введите коодинаты yB: ");
double yB = double.Parse(Console.ReadLine()!);

double result = Math.Sqrt(Math.Pow(xA - xB, 2) + Math.Pow(yA - yB, 2));
Console.WriteLine($"Расстояние между точками {result:f2}");

// через строку
result.ToString(("#.00"));
Console.Write($"Расстояние между точками {result:f2}");