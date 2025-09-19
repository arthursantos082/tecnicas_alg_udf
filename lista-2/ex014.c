#include <stdio.h>

int main() {
    float mediaMin, n1, n2, n3, mediaFinal;
    char nome[50];
    char sexo;

    // Solicita a média mínima
    printf("Digite a media para aprovacao: ");
    scanf("%f", &mediaMin);

    // Coleta os dados do aluno
    printf("Digite o nome do aluno: ");
    scanf(" %[^\n]", nome); // lê até espaço
    printf("Digite o sexo (M/F): ");
    scanf(" %c", &sexo);
    printf("Digite as tres notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);

    // Calcula a média
    mediaFinal = (n1 + n2 + n3) / 3;

    // Ajusta texto de acordo com o sexo
    if (mediaFinal >= mediaMin) {
        if (sexo == 'M' || sexo == 'm') {
            printf("O aluno %s foi aprovado com media %.2f\n", nome, mediaFinal);
        } else {
            printf("A aluna %s foi aprovada com media %.2f\n", nome, mediaFinal);
        }
    } else {
        if (sexo == 'M' || sexo == 'm') {
            printf("O aluno %s foi reprovado com media %.2f\n", nome, mediaFinal);
        } else {
            printf("A aluna %s foi reprovada com media %.2f\n", nome, mediaFinal);
        }
    }

    return 0;
}
