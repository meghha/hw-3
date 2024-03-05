# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "K-means clustering can be significantly influenced by outliers due to its reliance on mean-based centroid calculation, potentially leading to less reliable clustering results in the presence of outliers."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Agglomerative hierarchical clustering procedures, while deterministic in their approach to merging clusters based on proximity, can still sometimes result in different clusterings depending on the specific linkage criteria or distance metric used"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While it may not be true that K means is the most efficient clustering algorithm, it is indeed true that it fater than Agglomerative clustering. Agglomerative clustering is takes more time and memory than K means, more computationally intensive due to its quadratic or cubic time complexity, compared to the generally more efficient linear or slightly superlinear time complexity of K-means clustering"

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "K means algorithm works by assigning points to new centroid and recomputing centroids"

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "SSE is the sum of squared errors, which is the square of the distance between the data points in a cluster and its centroid. For more compact cohesive clusters, this value is low. That is, the more cohesion, the less is the SSE."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "SSB is the inter cluster distance, i.e., the disctance between the centroids of each cluster. As this increases, the seperation increases."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "This is false, because as the within cluster distance decreases, the inter cluster distance increases."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of SSE and SSB is equivalent to the variance of the data, which is a constant."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "True. SSE + SSB is a constant, and SSE is a representative of cohesion, while SSB is a representative for separation. As cohesion increases, i.e., SSE decreases, the SSB or separation increases."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * (R**2)"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + c**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10 * (R**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since all the three circles are equally spaced, as the convergence begins, each of the data points will be attached to the nearest centroid, and as they are recomputed, each of the circle will have its own centroid at the end of convergence."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "As the circles are equally spaced again, each of the data point will be attached to nearest centroid. Since A already has it owns centroid, points from C will be assigned to B's right centroid, and when the centroids are recomputed, each cluster will have its own centroid."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Here the real clusters are not equally spaced. Once the K means algorithm begins, points from Circle B will be assigned to Centroid in A, and when they are recomputed, the centroid will lie in between the two clusters. Centroid C will get to keep both centroids"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Single Linkage, also known as minimum linkage hierarchical clustering, is a method used to create a hierarchical clustering of a dataset. In this technique, the distance between two clusters is defined as the minimum distance between any single data point in the first cluster and any single data point in the second cluster. Since the shortest distance is between A and B, those two clusters would be combined first."

    # type: set
    answers["(b)"] = {"Group A","Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Complete Linkage, also known as maximum linkage hierarchical clustering, is another method used to create a hierarchical clustering of a dataset. In this technique, the distance between two clusters is defined as the maximum distance between any single data point in the first cluster and any single data point in the second cluster. Since Group A and Group C have the shortest complete linkage, those two are combined."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {"E" "B", "F", "J", "C", "L", "M", "I"}

    # type: set
    answers["(a) boundary"] = {"D","G"}

    # type: set
    answers["(a) noise"] = {"A","H"}

    # type: set
    answers["(b) cluster 1"] = {"B","C","E","F","G","D"}

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {"B","C","D","E","F","G","I","J","L","M"}

    # type: set
    answers["(c)-a boundary"] = {"A","H"}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] =  {"A"}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since cluster 4 exhibits the highest entropy, that is there is a disorder or uncertainty within that cluster regarding the distribution of classes. Lower values indicate better separation of classes within the cluster."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 exhibits lowest entropy."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Since the diagonal entries are the distances between the points of a cluster, within its own cluster, and they are predominantly blue, it idicates a strong cohesion in the clusters. It means that the clusters are tightly packed and well differentiated."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Since there are varying colours in the cross diagonal entries of row 1 and 3, it is represented by clusters A and C. Similar observation for Cluster B and cluster D"

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The distinct and mainly blue qualities of diagonal entries are noticeable, setting them apart from the rest. This suggests a strong cohesion within clusters B and C."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4 exhibit diverse colors, implying varying distances from other clusters, with less distinct diagonal entries. Rows 2 and 3 demonstrate identical colors, suggesting equidistant relationships with two clusters and a greater separation from one cluster."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries, are distinctly clear in blue and signify robust cohesion within clusters B and C. This consistency suggests stronger intra-cluster connections within these groups."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In every row, two off-diagonal entries share matching colors, while one entry differs in color. This suggests that each cluster is relatively closer to two other clusters compared to the third."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "All off-diagonal entries exhibit distinct colors, indicating varied distances from other clusters. Since Cluster A has a less distinct diagonal entry, it suggests that there is a weaker cohesion."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 represents Cluster B, as two out of three off-diagonal entries share matching colors, indicating equidistant relationships, notably between B and A, and B and C. The clearer diagonal entry suggests strong cohesion within this cluster, contrasting with B's distance from D"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 denotes Cluster C, as evidenced by the clearer diagonal entry, indicating strong cohesion within this cluster. Two out of three off-diagonal entries show matching colors, emphasizing equidistant relationships, especially between C and B, and C and D. Notably, C is more distant from A in comparison."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The off-diagonal entries of Cluster D display different colors, hence it is most prominent. It indicates varying distances from other clusters. The less defined diagonal entry implies weaker cohesion within this cluster, confirming its classification as Cluster D"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchial","overlapping","partial"]

    # type: list
    answers["(b)"] = ["partitional","exclusive","complete"]

    # type: list
    answers["(c)"] = ["partitional","fuzzy","complete"]

    # type: list
    answers["(d)"] = ["hierarchial","overlapping","partial"]

    # type: list
    answers["(e)"] = ["partitional","exclusive","partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Hierachial structure can be possible for students with similar scores"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN is used for clusters when they can be demarcated by high and low density regions. Since the features of the face, eyes, nose, and lips are within the high density region and are not separated they cannot be clustered well by DBSCAN for figure a. For figure b however, the dense regions are properly separated, which can be picked by DBSCAN techniquw."

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K means clustering should be used for clusters when they are clearly demarcated. In figure a, the cluster does not have clear boundaries , and instead it is just a cluster with gaps in it represented by the features of the face."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
