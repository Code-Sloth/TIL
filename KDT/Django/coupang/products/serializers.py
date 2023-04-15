# import serializers
# from .models import ProductImage, Product

# class ProductImageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(use_url=True)
#     class Meta:
#        model = ProductImage
#        fields = ['product_img']
      
# class ProductSerializer(serializers.ModelSerializer):
#     images = serializers.SerializerMethodField()
  
#     def get_images(self, obj):
#         image = obj.image.all() 
#         return ProductImageSerializer(instance=image, many=True, context=self.context).data

#     class Meta:
#         model = Product
#         fields = ('title', 'price', 'delivery_date', 'content', 'category','product_img',)

#     def create(self, validated_data):
#         instance = Product.objects.create(**validated_data)
#         image_set = self.context['request'].FILES
#         for image_data in image_set.getlist('product_img'):
#             ProductImage.objects.create(Product=instance, product_img=image_data)
#         return instance
   