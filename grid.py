from PIL import Image


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # generate grid, the size of width * height
        row = [0] * self.width
        self.grid = []
        for i in range(self.height):
            self.grid.append(list(row))

        self.output()

    def output(self):
        for row in self.grid:
            print(row)

    def draw(
            self, width: int, height: int, spacing: int,
            cell_color="#000",
            background_color="#666",
            head_color="#601e4b",
            tail_color="#1e5a60",
            fruit_color="#09ba1a"
    ):
        image_dimensions = self.width * width + (self.width + 1) * spacing, self.height * height + (self.height + 1) * spacing
        img = Image.new("RGB", image_dimensions, color=background_color)

        y = spacing
        for i in range(self.height):
            x = spacing
            for j in range(self.width):
                color = cell_color
                
                img.paste(Image.new("RGB", (width, height), color=color), (x, y))
                x += width + spacing

            y += height + spacing

        return img


if __name__ == '__main__':
    grid = Grid(20, 10)
    grid.draw(10, 10, 1).show()
