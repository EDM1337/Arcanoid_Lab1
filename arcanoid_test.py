from main import paddle, game_ball, is_game_over

import pytest


# Fixture for creating a player paddle object
@pytest.fixture
def create_player_paddle():
    return paddle()


# Fixture for creating a game ball object
@pytest.fixture
def create_game_ball(create_player_paddle):
    return game_ball(create_player_paddle.x +
                     (create_player_paddle.width // 2), create_player_paddle.y - create_player_paddle.height)


# Test case for the reset method of game_ball class
def test_game_ball_reset(create_player_paddle, create_game_ball):
    create_game_ball.reset(create_player_paddle.x +
                           (create_player_paddle.width // 2), create_player_paddle.y - create_player_paddle.height)
    assert create_game_ball.rect.x == create_player_paddle.x + \
           (create_player_paddle.width // 2) - create_game_ball.ball_rad
    assert create_game_ball.rect.y == create_player_paddle.y - create_player_paddle.height
    assert create_game_ball.speed_x == 4
    assert create_game_ball.speed_y == -4
    assert create_game_ball.game_over == 0


def test_ball_bounce_off_wall():
    game_ball_instance = game_ball(200, 300)  # Замініть `game_ball` на `game_ball_instance`

    # Set up the ball and simulate bouncing off the wall
    game_ball_instance.speed_x = -3
    game_ball_instance.rect.x = 0
    game_ball_instance.rect.y = 300

    game_ball_instance.bounce_off_wall()

    # Assert the expected outcome of the bounce
    assert game_ball_instance.speed_x > 0  # Ball should reverse its horizontal direction
    # Add more assertions as needed for other properties affected by the bounce


def test_game_over():
    # Передаємо необхідні параметри для перевірки
    game_over = True  # Припустимо, гра завершилась
    assert is_game_over(game_over) is True


pytest.main(["-v", "--html=report_arcanoid.html"])
