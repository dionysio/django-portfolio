from django.conf.urls import url


from .views import (
    HomeView,
    ArtworkDetailView, ArtworkListView,
    CollectionListView, CollectionDetailView,
    CategoryListView, CategoryDetailView
)


urlpatterns = [
    # Home view
    url(r'^$', HomeView.as_view(),
        name='portfolio_home'
    ),

    # Collection views
    url(r'^collections/$', CollectionListView.as_view(),
        name='collection_list'
    ),
    url(r'^collections/<slug:s>/', CollectionDetailView.as_view(),
        name='collection_detail'
    ),

    # Artwork views
    url(r'^works/$', ArtworkListView.as_view(),
        name='artwork_list'
    ),
    url(r'^works/<pk:#>/$', ArtworkDetailView.as_view(),
        name='artwork_detail'
    ),

    # Category views
    url(r'^category/$', CategoryListView.as_view(),
        name='category_list'
    ),
    url(r'^category/<slug:s>/', CategoryDetailView.as_view(),
        name='category_detail'
    )
]
