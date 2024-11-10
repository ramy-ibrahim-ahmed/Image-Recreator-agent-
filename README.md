# 🎨 Image Recreation Using Evolutionary Algorithms

## 🌟 Project Overview
In this project, we explore the fascinating intersection of computer science and digital art by recreating images through the use of **evolutionary algorithms**. By mimicking natural selection, our system evolves a population of images over generations to closely resemble a target image. This innovative approach highlights the power of evolutionary computing in generating visually compelling results.

![Mona Lisa Evolution](mona_lisa.gif)

## 🖼️ Representation
Each individual in the population is represented as:
- A **picture** composed of a set number of polygons.
- **Polygons** are randomly placed and colored within the image boundaries, ensuring that their positions do not extend outside the image frame.
- **Color Randomization**: Polygons are assigned random colors, contributing to the diverse genetic makeup of individuals.

## 🔄 Variation Methods
### 1. One-Point Crossover
- **Mechanism**: Selects a random point to split two parent images and create a child.
- **Cutting Options**: The cutting point can be either vertical or horizontal, and its position is chosen randomly.
- **Outcome**: The resulting child inherits parts of each parent, blending their features in a unique configuration.

### 2. Blending Crossover
- **Mechanism**: Generates a child image by blending the pixel values of two parents using a random alpha (α) value.
- **Alpha Range**: A random coefficient between 0 and 1 that determines the weight of each parent's contribution.
- **Outcome**: Smooth merging of parental traits, yielding subtle color transitions and nuanced results.

### 3. Add Random Polygons Mutation
- **Mechanism**: Introduces additional polygons into the image, constrained by a maximum allowable number to prevent overcrowding.
- **Purpose**: Introduces genetic diversity, enabling new shapes and colors that may enhance image resemblance to the target.
- **Constraints**: The maximum number of polygons is decreased over generations to balance exploration and exploitation.

## 📊 Evaluation Method
To measure how closely an individual matches the target image, the **CIE1976 Delta E** formula is employed:
- **Color Difference Calculation**: Computes the perceptual difference between corresponding pixels of the target image and an individual.
- **Mean Difference**: The mean of all pixel differences is used as the individual's fitness score, with lower values indicating a closer match to the target.

## 🤖 Parent Selection: Tournament Selection
- **Process**: Selects 6 random individuals from the current population and compares their fitness.
- **Winner Selection**: The individual with the best fitness among the selected is chosen as a parent.
- **Advantage**: Encourages healthy competition, promoting stronger genetic material to propagate.

## 🏆 Survivors' Selection: Elitism Strategy
- **Methodology**: Ensures that the best-performing individuals from the current generation are carried over to the next.
- **Integration with Variation**: After applying the variation methods (crossover and mutation), the offspring are evaluated and added to the new generation.
- **Population Control**: This cycle continues until the new generation reaches the designated population size, preserving a balance between innovation and consistency.

## 🛠️ Implementation Technologies
- **Python**: Core programming language for building and running the evolutionary algorithm.
- **NumPy**: Efficient array operations and mathematical functions.
- **PIL (Pillow)**: Image handling for reading, processing, and displaying images.
- **Matplotlib**: Visualization of evolution progress, fitness scores, and output images.

## 🖌️ Visual Output
The project evolves from an abstract initial population to increasingly detailed recreations of the target image over generations. 

### Example Output:
1. **Initial Generation**: Randomly composed images with no resemblance to the target.
2. **Intermediate Generations**: Shapes and colors begin to align with the target as the algorithm refines the individuals.
3. **Final Generation**: A visually striking recreation that closely matches the target image, highlighting the effectiveness of evolutionary strategies.

## 🚧 Challenges and Insights
- **Balancing Exploration and Exploitation**: Adjusting mutation rates and the maximum number of polygons to ensure that the algorithm explores enough solutions while honing in on promising areas.
- **Performance**: Fine-tuning the tournament size and blending coefficients to avoid premature convergence and maintain diversity.
- **Evaluation Efficiency**: Optimizing the fitness evaluation for large image sizes to keep computation times reasonable.

## 🔮 Future Enhancements
- **Parallel Processing**: Speed up the evolutionary process by running evaluations and variations in parallel.
- **Interactive GUI**: Create a user interface for real-time visualization and parameter adjustment.
- **Multi-Objective Optimization**: Incorporate additional fitness metrics such as edge detection and texture similarity for more sophisticated recreations.
- **Dynamic Polygon Counts**: Adjust the number of polygons based on the generation's performance to adaptively fine-tune complexity.

## 📬 Contact
For questions or suggestions, feel free to reach out via [Mail](ramyibrahim987@gmail.com)
