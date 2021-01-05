from Bird import Bird
from Pipe import Pipe
from Base import Base
from global_var import *
from draw_window import draw_window


def main():
    birds = Bird(230, 350)

    base = Base(730)
    pipes = [Pipe(700)]
    score = 0

    win = pygame.display.set_mode((WIN_WIDTH, 800))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYUP:
                birds.jump()
            elif event.type == pygame.QUIT:
                print_score(score)
                run = False
                pygame.quit()
                quit()

        birds.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(birds):
                print_score(score)
                pygame.quit()
                quit()

            if not pipe.passed and pipe.x < birds.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        if birds.y + birds.img.get_height() >= 730 or birds.y < 0:
            print_score(score)
            pygame.quit()
            quit()

        base.move()
        draw_window(win, birds, pipes, base, score)


def print_score(score):
    print("You lost! your score is " + str(score))
