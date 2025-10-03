from pathlib import Path

from matplotlib import pyplot

from political_party_analysis.loader import DataLoader
from political_party_analysis.dim_reducer import DimensionalityReducer
from political_party_analysis.estimator import DensityEstimator
from political_party_analysis.visualization import (
    scatter_plot,
    plot_density_estimation_results,
    plot_finnish_parties,
)

if __name__ == "__main__":

    data_loader = DataLoader()
    # Data pre-processing step
    ##### YOUR CODE GOES HERE #####
    data_loader.preprocess_data()

    # Dimensionality reduction step
    ##### YOUR CODE GOES HERE #####
    dim_reducer = DimensionalityReducer("PCA", data_loader.party_data, 2)
    reduced_dim_data = dim_reducer.transform()

    ## Uncomment this snippet to plot dim reduced data
    pyplot.figure()
    splot = pyplot.subplot()
    scatter_plot(
        reduced_dim_data,
        color="r",
        splot=splot,
        label=["dim reduced data"],
    )
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "dim_reduced_data.png"]))

    # Density estimation/distribution modelling step
    ##### YOUR CODE GOES HERE #####
    estimator = DensityEstimator(
        data_loader.party_data,
        dim_reducer=dim_reducer,
        high_dim_feature_names=data_loader.party_data.columns,
    )
    estimator.fit()
    new_parties_low_dim = estimator.sample_parties()
    new_parties_high_dim = estimator.inverse_transform_samples(new_parties_low_dim)

    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    predictions = estimator.model.predict(reduced_dim_data)
    plot_density_estimation_results(
        X=new_parties_high_dim,
        Y_=predictions,
        means=estimator.model.means_,
        covariances=estimator.model.covariances_,
        title="GMM Density Estimation of Political Parties",
    )
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "density_estimation.png"]))

    # Plot left and right wing parties here
    lr_cols = ["lrgen", "lrecon"]

    # Check which of the columns are available in the preprocessed data
    existing_lr_cols = [col for col in lr_cols if col in data_loader.party_data.columns]
    # Create a composite score. Since data is scaled, a value <= 0 can be
    # considered left-of-center and > 0 as right-of-center.
    lr_score = data_loader.party_data[existing_lr_cols].mean(axis=1)
    left_mask = lr_score <= 0
    right_mask = lr_score > 0
    pyplot.figure()
    splot = pyplot.subplot()
    ##### YOUR CODE GOES HERE #####
    # Plot left-wing parties in blue
    scatter_plot(reduced_dim_data[left_mask], color="blue", splot=splot, label=["Left-wing"])

    # Plot right-wing parties in red
    scatter_plot(reduced_dim_data[right_mask], color="red", splot=splot, label=["Right-wing"])
    pyplot.title("Lefty/righty parties")
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "left_right_parties.png"]))

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####
    pyplot.figure()
    splot = pyplot.subplot()
    # First plot all parties as a grey background for context
    scatter_plot(reduced_dim_data, color="grey", splot=splot, label=["All Parties"], size=5)
    # Then plot the Finnish parties on top
    plot_finnish_parties(reduced_dim_data, splot=splot)
    pyplot.title("Finnish Parties in the European Political Landscape")
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "finnish_parties.png"]))

    print("Analysis Complete")
